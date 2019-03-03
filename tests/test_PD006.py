"""
Test to check for use of explicit comparison methods.  

Recommend use of binary comparison operators instead.
"""
import ast

from pandas_vet import VetPlugin
from pandas_vet import PD006


def test_PD006_pass_comparison_operator():
    """
    Test that using binary comparison operator explicitly does not result in an error.
    """
    comparison_operators = ['>',  '<',  '>=', '<=', '==', '!=']
    for op in comparison_operators:
        statement = f'C = A {op} B'
        tree = ast.parse(statement)
        actual = list(VetPlugin(tree).run())
        expected = []
        assert actual == expected


def test_PD006_fail_comparison_method():
    """
    Test that using comparison method results in an error.
    """
    comparison_methods = ['gt', 'lt', 'ge', 'le', 'eq', 'ne']
    for op in comparison_methods:
        statement = f'C = A.{op}(B)'
        tree = ast.parse(statement)
        actual = list(VetPlugin(tree).run())
        expected = [PD006(1, 4)]
        assert actual == expected


