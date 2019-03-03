# stdlib
import ast

from pandas_vet import VetPlugin
from pandas_vet import PD007


def test_PD007_pass_loc():
    """
    Test that using .loc[] explicitly does not result in an error.
    """
    statement = "new_df = df.loc['d':, 'A':'C']"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = []
    assert actual == expected


def test_PD007_pass_iloc():
    """
    Test that using .iloc[] explicitly does not result in an error.
    """
    statement = "new_df = df.iloc[[1, 3, 5], [1, 3]]"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = []
    assert actual == expected


def test_PD007_fail():
    """
    Test that using .ix[] results in an error.
    """
    statement = "s = df.ix[[0, 2], 'A']"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = [PD007(1, 4)]
    assert actual == expected
