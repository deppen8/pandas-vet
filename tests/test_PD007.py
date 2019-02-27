# stdlib
import ast

from pandas_vet import VetPlugin
from pandas_vet import PD007


def test_PD007_pass_loc():
    """
    Test that using .loc() explicitly does not result in an error.
    """
    statement = "index = pd.loc(val)"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = []
    assert actual == expected


def test_PD007_pass_iloc():
    """
    Test that using .iloc() explicitly does not result in an error.
    """
    statement = "index = pd.iloc(val)"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = []
    assert actual == expected


def test_PD007_fail():
    """
    Test that using .ix() results in an error.
    """
    statement = "index = pd.ix(val)"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = [PD007(1, 8)]
    assert actual == expected


