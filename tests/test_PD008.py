# stdlib
import ast

from pandas_vet import VetPlugin
from pandas_vet import PD001, PD002, PD003, PD004, PD008


def test_PD008_pass():
    """
    Test that using .loc() explicitly does not result in an error.
    """
    statement = "index = df.loc(val)"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = []
    assert actual == expected


def test_PD008_fail():
    """
    Test that using .at() results in an error.
    """
    statement = "index = df.at(val)"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = [PD008(1, 8)]
    assert actual == expected


