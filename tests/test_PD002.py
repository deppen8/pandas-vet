# stdlib
import ast

from pandas_vet import PD002, VetPlugin


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
