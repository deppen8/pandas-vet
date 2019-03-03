# stdlib
import ast

from pandas_vet import VetPlugin
from pandas_vet import PD008


def test_PD008_pass():
    """
    Test that using .loc[] explicitly does not result in an error.
    """
    statement = "index = df.loc[:, ['B', 'A']]"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = []
    assert actual == expected


def test_PD008_fail():
    """
    Test that using .at[] results in an error.
    """
    statement = "index = df.at[:, ['B', 'A']]"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = [PD008(1, 8)]
    assert actual == expected

    
def test_PD008_node_value_Name_pass():
    """
    Test that an ast.Subscript where node.value is a Name does NOT raise an error
    """
    statement = "s = at[[0, 2], 'A']"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = []
    assert actual == expected
