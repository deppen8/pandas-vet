# stdlib
import ast

from pandas_vet import VetPlugin
from pandas_vet import PD009


def test_PD009_pass():
    """
    Test that using .iloc[] explicitly does not result in an error.
    """
    statement = "index = df.iloc[:, 1:3]"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = []
    assert actual == expected


def test_PD009_fail():
    """
    Test that using .iat[] results in an error.
    """
    statement = "index = df.iat[:, 1:3]"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = [PD009(1, 8)]
    assert actual == expected


def test_PD009_node_value_Name_pass():
    """
    Test that an ast.Subscript where node.value is a Name does NOT raise an error
    """
    statement = "s = iat[[0, 2], 'A']"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = []
    assert actual == expected
