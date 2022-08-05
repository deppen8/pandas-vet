# stdlib
import ast

from pandas_vet import VetPlugin
from pandas_vet import PD002


def test_PD002_pass():
    """
    Test that using inplace=False explicitly does not result in an error.
    """
    statement = """df.drop(['a'], axis=1, inplace=False)"""
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = []
    assert actual == expected


def test_PD002_fail():
    """
    Test that using inplace=True results in an error.
    """
    statement = """df.drop(['a'], axis=1, inplace=True)"""
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = [PD002(1, 0)]
    assert actual == expected


def test_PD002_with_variable_does_not_crash():
    """
    Test that using inplace=<some variable> does not raise Exceptions.

    It will not be able to infer the value of the variable, so no errors either.
    """
    statement = """use_inplace=True; df.drop(['a'], axis=1, inplace=use_inplace)"""
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = []
    assert actual == expected
