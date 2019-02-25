import ast
from collections import namedtuple
from functools import partial
from typing import List

import attr


@attr.s
class Visitor(ast.NodeVisitor):
    """
    ast.NodeVisitor will automatically call the appropriate method for a given node type

    i.e. calling self.visit on an Import node calls visit_import
    """
    errors = attr.ib(default=attr.Factory(list))

    def visit_Import(self, node):
        self.generic_visit(node)  # continue checking children
        self.errors.extend(check_import_name(node))

    def visit_Call(self, node):
        self.generic_visit(node)  # continue checking children
        self.errors.extend(check_inplace_false(node))

    def check(self, node):
        self.errors = []
        self.visit(node)
        return self.errors


class VetPlugin:
    name = "flake8-pandas-vet"
    version = "0.1.0"

    def __init__(self, tree):
        self.tree = tree

    def run(self):
        return Visitor().check(self.tree)


def check_import_name(node: ast.Import) -> List:
    errors = []
    for n in node.names:
        if n.name == "pandas" and n.asname != "pd":
            errors.append(PD001(node.lineno, node.col_offset))
    return errors


def check_inplace_false(node: ast.Import) -> List:
    errors = []
    for kw in node.keywords:
        if kw.arg == "inplace" and kw.value.value is True:
            errors.append(PD002(node.lineno, node.col_offset))
    return errors


error = namedtuple("Error", ["lineno", "col", "message", "type"])
Error = partial(partial, error, type=VetPlugin)

PD001 = Error(
    message="PD001 pandas should always be imported as 'import pandas as pd'"
)
PD002 = Error(
    message="'inplace = True' should be avoided; it has inconsistent behavior"
)
PD003 = Error(
    "'.isna' is preferred to '.isnull'; functionality is equivalent"
)
PD004 = Error(
    "'.notna' is preferred to '.notnull'; functionality is equivalent"
)
PD005 = Error(
    "Use arithmetic operator instead of method"
)
PD006 = Error(
    "Use comparison operator instead of method"
)
