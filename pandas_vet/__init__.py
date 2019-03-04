import ast
from collections import namedtuple
from functools import partial
from typing import List

import attr

from .version import __version__


@attr.s
class Visitor(ast.NodeVisitor):
    """
    ast.NodeVisitor will automatically call the appropriate method for a given node type

    i.e. calling self.visit on an Import node calls visit_import
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
        self.errors.extend(check_for_values(node))

    def check(self, node):
        self.errors = []
        self.visit(node)
        return self.errors


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


def check_import_name(node: ast.Import) -> List:
    errors = []
    for n in node.names:
        if n.name == "pandas" and n.asname != "pd":
            errors.append(PD001(node.lineno, node.col_offset))
    return errors


def check_inplace_false(node: ast.Call) -> List:
    errors = []
    for kw in node.keywords:
        if kw.arg == "inplace" and kw.value.value is True:
            errors.append(PD002(node.lineno, node.col_offset))
    return errors


def check_for_isnull(node: ast.Call) -> List:
    if isinstance(node.func, ast.Attribute) and node.func.attr == "isnull":
        return [PD003(node.lineno, node.col_offset)]
    return []


def check_for_notnull(node: ast.Call) -> List:
    if isinstance(node.func, ast.Attribute) and node.func.attr == "notnull":
        return [PD004(node.lineno, node.col_offset)]
    return []

def check_for_ix(node: ast.Subscript) -> List:
    if node.value.attr == "ix":
        return [PD007(node.lineno, node.col_offset)]
    return []


def check_for_at(node: ast.Call) -> List:
    if node.value.attr == "at":
        return [PD008(node.lineno, node.col_offset)]
    return []


def check_for_iat(node: ast.Call) -> List:
    if node.value.attr == "iat":
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
    Check AST for occurence of the `.unstack()` method on the pandas data frame.

    Error/warning message to recommend use of `.pivot_table()` method instead.
    """
    if isinstance(node.func, ast.Attribute) and node.func.attr == "unstack":
        return [PD010(node.lineno, node.col_offset)]
    return []


def check_for_values(node: ast.Attribute) -> List:
    """
    Check AST for occurence of the `.values` attribute on the pandas data frame.

    Error/warning message to recommend use of `.array` data frame attribute for
    PandasArray, or `.to_array()` method for NumPy array.
    """
    if node.attr == "values":
        return [PD011(node.lineno, node.col_offset)]
    return []


error = namedtuple("Error", ["lineno", "col", "message", "type"])
VetError = partial(partial, error, type=VetPlugin)

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
PD005 = VetError(
    message="PD005 Use arithmetic operator instead of method"
)
PD006 = VetError(
    message="PD006 Use comparison operator instead of method"
)
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
    message="PD010 '.pivot_table' is preferred to '.pivot' or '.unstack'; provides same functionality"
)
PD011 = VetError(
    message="PD011 Use '.array' or '.to_array()' instead of '.values'; 'values' is ambiguous"
)
