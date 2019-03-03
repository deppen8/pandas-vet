"""
Test to check for use of explicit arithmetic methods.  

Recommend use of binary arithmetic operators instead.
"""
import ast

from pandas_vet import VetPlugin
from pandas_vet import PD005


def test_PD005_pass_arithmetic_operator():
    """
    Test that using binary aritmetic operator explicitly does not result in an error.
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
        statement = f'C = A {op} B'
        tree = ast.parse(statement)
        actual = list(VetPlugin(tree).run())
        expected = []
        assert actual == expected


def test_PD005_fail_arithmetic_method():
    """
    Test that using aritmetic method results in an error.
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
        statement = f'C = A.{op}(B)'
        tree = ast.parse(statement)
        actual = list(VetPlugin(tree).run())
        expected = [PD005(1, 4)]
        assert actual == expected


