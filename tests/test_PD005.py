"""
Test to check for use of explicit arithmetic methods.

Recommend use of binary arithmetic operators instead.
"""
import ast

from pandas_vet import VetPlugin
from pandas_vet import PD005


def test_PD005_pass_arithmetic_operator():
    """
    Test that using binary arithmetic operator explicitly does not result in an error.
    """
    arithmetic_operators = [
        '+',
        '-',
        '*',
        '/',
        '**',
        '//',
        '%',
        ]
    for op in arithmetic_operators:
        statement = 'C = A {0} B'.format(op)
        tree = ast.parse(statement)
        actual = list(VetPlugin(tree).run())
        expected = []
        assert actual == expected


def test_PD005_fail_arithmetic_method():
    """
    Test that using arithmetic method results in an error.
    """
    arithmetic_methods = [
        'add',
        'sub', 'subtract',
        'mul', 'multiply',
        'div', 'divide', 'truediv',
        'pow',
        'floordiv',
        'mod',
        ]
    for op in arithmetic_methods:
        statement = 'C = A.{0}(B)'.format(op)
        tree = ast.parse(statement)
        actual = list(VetPlugin(tree).run())
        expected = [PD005(1, 4)]
        assert actual == expected
