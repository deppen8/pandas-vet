import ast
from collections import namedtuple
from functools import partial
from typing import List

import attr

from .version import __version__


@attr.s
class Visitor(ast.NodeVisitor):
    """
    ast.NodeVisitor calls the appropriate method for a given node type

    i.e. calling self.visit on an Import node calls visit_import

    The `check` functions should be called from the `visit_` method that
    would produce a 'fail' condition.
    """

    errors = attr.ib(default=attr.Factory(list))

    def visit_Import(self, node):
        """
        Called for `import ..` and `import .. as ..` nodes.
        """
        self.generic_visit(node)  # continue checking children
        self.errors.extend(check_import_name(node))

    def visit_Call(self, node):
        """
        Called for `.method()` nodes.
        """
        self.generic_visit(node)  # continue checking children
        self.errors.extend(check_inplace_false(node))
        self.errors.extend(check_for_isnull(node))
        self.errors.extend(check_for_notnull(node))
        self.errors.extend(check_for_pivot(node))
        self.errors.extend(check_for_unstack(node))
        self.errors.extend(check_for_stack(node))
        self.errors.extend(check_for_arithmetic_methods(node))
        self.errors.extend(check_for_comparison_methods(node))
        self.errors.extend(check_for_read_table(node))
        self.errors.extend(check_for_merge(node))

    def visit_Subscript(self, node):
        """
        Called for `[slicing]` nodes.
        """
        self.generic_visit(node)  # continue checking children
        self.errors.extend(check_for_ix(node))
        self.errors.extend(check_for_at(node))
        self.errors.extend(check_for_iat(node))

    def visit_Attribute(self, node):
        """
        Called for `.attribute` nodes.
        """
        self.generic_visit(node)  # continue checking children
        self.errors.extend(check_for_values(node))

    def visit_Name(self, node):
        """
        Called for `Assignment` nodes.
        """
        self.generic_visit(node)  # continue checking children
        self.errors.extend(check_for_df(node))

    def check(self, node):
        self.errors = []
        self.visit(node)
        return self.errors

    def generic_visit(self, node):
        """Called if no explicit visitor function exists for a node.

        This also attaches breadcrumbs before visiting a node so we can
        later look up the syntax tree. This way, there's more
        information to decide whether or not to raise.

        The breadcrumb name is `__pandas_vet_parent` (name mangled) to
        avoid all reasonable name collisions.

        .. seealso:: `check_for_values`.
        """
        for field, value in ast.iter_fields(node):
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, ast.AST):
                        item.__pandas_vet_parent = node
                        self.visit(item)
            elif isinstance(value, ast.AST):
                value.__pandas_vet_parent = node
                self.visit(value)


class PandasVetException(Exception):
    pass


class VetPlugin:
    name = "flake8-pandas-vet"
    version = __version__

    def __init__(self, tree):
        self.tree = tree

    def run(self):
        try:
            return Visitor().check(self.tree)
        except Exception as e:
            raise PandasVetException(e)

    @staticmethod
    def add_options(optmanager):
        """Informs flake8 to ignore PD9xx by default."""
        optmanager.extend_default_ignore(disabled_by_default)

        optmanager.add_option(
            long_option_name="--annoy",
            action="store_true",
            dest="annoy",
            default=False,
        )

    @staticmethod
    def parse_options(optmanager, options, args):
        """Receives the parsed options and values."""
        if not options.annoy:
            return
        for v in disabled_by_default:
            try:
                options.ignore.remove(v)
            except ValueError:
                pass


def check_import_name(node: ast.Import) -> List:
    """Check AST for imports of pandas not using the preferred alias 'pd'.

    Error/warning message to recommend use of 'pd' alias.

    :param node: an AST node of type Import
    :return errors: list of errors of type PD001 with line number and column offset
    """
    errors = []
    for n in node.names:
        if n.name == "pandas" and n.asname != "pd":
            errors.append(PD001(node.lineno, node.col_offset))
    return errors


def check_inplace_false(node: ast.Call) -> List:
    """Check AST for function calls using inplace=True keyword argument.

    Disapproved:
        df.method(inplace=True)

    Approved:
        df = df.method(inplace=False)

    Error/warning message to recommend avoidance of inplace=True due to inconsistent behavior.

    :param node: an AST node of type Call
    :return errors: list of errors of type PD002 with line number and column offset
    """
    errors = []
    for kw in node.keywords:
        if kw.arg == "inplace" and kw.value.value is True:
            errors.append(PD002(node.lineno, node.col_offset))
    return errors


def check_for_isnull(node: ast.Call) -> List:
    """Check AST for function calls using the isnull() method.

    Disapproved:
        df.isnull()

    Approved:
        df.isna()

    Error/warning message to recommend usage of .isna() instead of .isnull().
    Functionality is equivalent.

    :param node: an AST node of type Call
    :return errors: list of errors of type PD003 with line number and column offset
    """
    if isinstance(node.func, ast.Attribute) and node.func.attr == "isnull":
        return [PD003(node.lineno, node.col_offset)]
    return []


def check_for_notnull(node: ast.Call) -> List:
    """Check AST for function calls using the notnull() method.

    Disapproved:
        df.notnull()

    Approved:
        df.notna()

    Error/warning message to recommend usage of .notna() instead of .notnull().
    Functionality is equivalent.

    :param node: an AST node of type Call
    :return errors: list of errors of type PD004 with line number and column offset
    """
    if isinstance(node.func, ast.Attribute) and node.func.attr == "notnull":
        return [PD004(node.lineno, node.col_offset)]
    return []


def check_for_arithmetic_methods(node: ast.Call) -> List:
    """
    Check AST for occurence of explicit arithmetic methods.

    Error/warning message to recommend use of binary arithmetic operators.
    """
    arithmetic_methods = [
        "add",
        "sub",
        "subtract",
        "mul",
        "multiply",
        "div",
        "divide",
        "truediv",
        "pow",
        "floordiv",
        "mod",
    ]

    if isinstance(node.func, ast.Attribute) and node.func.attr in arithmetic_methods:
        return [PD005(node.lineno, node.col_offset)]
    return []


def check_for_comparison_methods(node: ast.Call) -> List:
    """
    Check AST for occurence of explicit comparison methods.

    Error/warning message to recommend use of binary comparison operators.
    """
    comparison_methods = ["gt", "lt", "ge", "le", "eq", "ne"]

    if isinstance(node.func, ast.Attribute) and node.func.attr in comparison_methods:
        return [PD006(node.lineno, node.col_offset)]
    return []


def check_for_ix(node: ast.Subscript) -> List:
    """
    Check AST for use of deprecated `.ix[]` attribute on data frame.

    Error/warning message to recommend use of explicit `.iloc[]` or `.loc[]` instead.
    """
    if isinstance(node.value, ast.Attribute) and node.value.attr == "ix":
        return [PD007(node.lineno, node.col_offset)]
    return []


def check_for_at(node: ast.Subscript) -> List:
    """
    Check AST for use of deprecated `.at[]` attribute on data frame.

    Error/warning message to recommend use of explicit `.loc[]` instead.
    """
    if isinstance(node.value, ast.Attribute) and node.value.attr == "at":
        return [PD008(node.lineno, node.col_offset)]
    return []


def check_for_iat(node: ast.Subscript) -> List:
    """
    Check AST for use of deprecated `.iat[]` attribute on data frame.

    Error/warning message to recommend use of explicit `.iloc[]` instead.
    """
    if isinstance(node.value, ast.Attribute) and node.value.attr == "iat":
        return [PD009(node.lineno, node.col_offset)]
    return []


def check_for_pivot(node: ast.Call) -> List:
    """
    Check AST for occurence of the `.pivot()` method on the pandas data frame.

    Error/warning message to recommend use of `.pivot_table()` method instead.
    This check should work for both the `df.pivot()` method, as well as the
    `pd.pivot(df)` function.
    """
    if isinstance(node.func, ast.Attribute) and node.func.attr == "pivot":
        return [PD010(node.lineno, node.col_offset)]
    return []


def check_for_unstack(node: ast.Call) -> List:
    """
    Check occurence of the `.unstack()` method on the pandas data frame.

    Error/warning message to recommend use of `.pivot_table()` method.
    """
    if isinstance(node.func, ast.Attribute) and node.func.attr == "unstack":
        return [PD010(node.lineno, node.col_offset)]
    return []


def check_for_stack(node: ast.Call) -> List:
    """
    Check AST for occurence of the `.stack()` method on the pandas data frame.

    Error/warning message to recommend use of `.melt()` method instead.
    """
    if isinstance(node.func, ast.Attribute) and node.func.attr == "stack":
        return [PD013(node.lineno, node.col_offset)]
    return []


def check_for_values(node: ast.Attribute) -> List:
    """
    Check occurence of the `.values` attribute on the pandas data frame.

    Error/warning message to recommend use of `.array` data frame attribute
    for PandasArray, or `.to_array()` method for NumPy array.

    In order to discriminate `df.values` (where this check should raise) vs
    calls, like `dict().values()` (where this should not), this function
    needs to check the node breadcrumb defined at `Visitor.generic_visit`,
    raising only in the first case.

    .. seealso:: `Visitor.generic_visit`.
    """
    if node.attr == "values":
        parent = getattr(node, "_Visitor__pandas_vet_parent", None)
        if (
            parent
            and isinstance(parent, ast.Call)
            and isinstance(parent.func, ast.Attribute)
            and parent.func.attr == "values"
        ):
            return []
        return [PD011(node.lineno, node.col_offset)]
    return []


def check_for_read_table(node: ast.Call) -> List:
    """
    Check AST for occurence of the `.read_table()` method on the pandas object.

    Error/warning message to recommend use of `.read_csv()` method instead.
    """
    if isinstance(node.func, ast.Attribute) and node.func.attr == "read_table":
        return [PD012(node.lineno, node.col_offset)]
    return []


def check_for_merge(node: ast.Call) -> List:
    """
    Check for use of `.merge()` method on the pandas object.

    Error/warning message to recommend use of `df.merge()` method instead.
    """
    # The AST does not retain any of the pandas semantic information, so the
    # current implementation of this test will infer based on the name of the
    # object.  If the object name is `pd`, and if the `.merge()` method has at
    # least two arguments (left, right, ... ) we will assume that it matches
    # the pattern that we are trying to check, `pd.merge(left, right)`
    if not hasattr(node.func, "value"):
        return []  # ignore functions
    elif not hasattr(node.func.value, "id"):
        return []  # it could be the case that id is not present

    if node.func.value.id != "pd":
        return []  # assume object name is `pd`

    if not len(node.args) >= 2:
        return []  # at least two arguments

    if isinstance(node.func, ast.Attribute) and node.func.attr == "merge":
        return [PD015(node.lineno, node.col_offset)]
    return []


def check_for_df(node: ast.Name) -> List:
    """
    Check for variables named `df`
    """
    if node.id == "df" and isinstance(node.ctx, ast.Store):
        return [PD901(node.lineno, node.col_offset)]
    return []


error = namedtuple("Error", ["lineno", "col", "message", "type"])
VetError = partial(partial, error, type=VetPlugin)

disabled_by_default = ["PD9"]

PD001 = VetError(
    message="PD001 pandas should always be imported as 'import pandas as pd'"
)

PD002 = VetError(
    message="PD002 'inplace = True' should be avoided; it has inconsistent behavior"
)

PD003 = VetError(
    message="PD003 '.isna' is preferred to '.isnull'; functionality is equivalent"
)

PD004 = VetError(
    message="PD004 '.notna' is preferred to '.notnull'; functionality is equivalent"
)
PD005 = VetError(message="PD005 Use arithmetic operator instead of method")

PD006 = VetError(message="PD006 Use comparison operator instead of method")

PD007 = VetError(
    message="PD007 '.ix' is deprecated; use more explicit '.loc' or '.iloc'"
)
PD008 = VetError(
    message="PD008 Use '.loc' instead of '.at'.  If speed is important, use numpy."
)
PD009 = VetError(
    message="PD009 Use '.iloc' instead of '.iat'.  If speed is important, use numpy."
)
PD010 = VetError(
    message="PD010 '.pivot_table' is preferred to '.pivot' or '.unstack'; "
    "provides same functionality"
)
PD011 = VetError(
    message="PD011 Use '.array' or '.to_array()' instead of '.values'; 'values' is ambiguous"
)
PD012 = VetError(
    message="PDO12 '.read_csv' is preferred to '.read_table'; provides same functionality"
)
PD013 = VetError(
    message="PD013 '.melt' is preferred to '.stack'; provides same functionality"
)
PD015 = VetError(
    message="PD015 Use '.merge' method instead of 'pd.merge' function. "
    "They have equivalent functionality."
)

PD901 = VetError(
    message="PD901 'df' is a bad variable name. Be kinder to your future self."
)
