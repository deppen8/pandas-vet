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
        self.generic_visit(node)  # continue checking children
        self.errors.extend(check_import_name(node))

    def visit_Call(self, node):
        self.generic_visit(node)  # continue checking children
        self.errors.extend(check_inplace_false(node))
        self.errors.extend(check_for_isnull(node))
        self.errors.extend(check_for_notnull(node))

    def visit_Subscript(self, node):
        self.generic_visit(node)  # continue checking children
        self.errors.extend(check_for_ix(node))
        self.errors.extend(check_for_at(node))
        self.errors.extend(check_for_iat(node))

    def check(self, node):
        self.errors = []
        self.visit(node)
        return self.errors


class VetPlugin:
    name = "flake8-pandas-vet"
    version = __version__

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


def check_inplace_false(node: ast.Call) -> List:
    errors = []
    for kw in node.keywords:
        if kw.arg == "inplace" and kw.value.value is True:
            errors.append(PD002(node.lineno, node.col_offset))
    return errors


def check_for_isnull(node: ast.Call) -> List:
    errors = []
    if node.func.attr == "isnull":
        errors.append(PD003(node.lineno, node.col_offset))
    return errors


def check_for_notnull(node: ast.Call) -> List:
    errors = []
    if node.func.attr == "notnull":
        errors.append(PD004(node.lineno, node.col_offset))
    return errors


def check_for_ix(node: ast.Subscript) -> List:
    errors = []
    if node.value.attr == "ix":
        errors.append(PD007(node.lineno, node.col_offset))
    return errors

  
def check_for_at(node: ast.Call) -> List:
    errors = []
    if node.value.attr == "at":
        errors.append(PD008(node.lineno, node.col_offset))
    return errors


def check_for_iat(node: ast.Call) -> List:
    errors = []
    if node.value.attr == "iat":
        errors.append(PD009(node.lineno, node.col_offset))
    return errors


error = namedtuple("Error", ["lineno", "col", "message", "type"])
VetError = partial(partial, error, type=VetPlugin)

PD001 = VetError(
    message="PD001 pandas should always be imported as 'import pandas as pd'"
)
PD002 = VetError(
    message="'inplace = True' should be avoided; it has inconsistent behavior"
)
PD003 = VetError(
    message="'.isna' is preferred to '.isnull'; functionality is equivalent"
)
PD004 = VetError(
    message="'.notna' is preferred to '.notnull'; functionality is equivalent"
)
PD005 = VetError(
    message="Use arithmetic operator instead of method"
)
PD006 = VetError(
    message="Use comparison operator instead of method"
)

PD007 = VetError(
    message="'.ix' is deprecated; use more explicit '.loc' or '.iloc'"
)

PD008 = VetError(
    message="Use '.loc' instead of '.at'.  If speed is important, use numpy."
)
PD009 = VetError(
    message="Use '.iloc' instead of '.iat'.  If speed is important, use numpy."
)
