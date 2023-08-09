# stdlib
import ast

from pandas_vet import PD004, VetPlugin


def test_PD004_pass():
    """
    Test that using .notna() explicitly does not result in an error.
    """
    statement = "notnas = pd.notna(val)"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = []
    assert actual == expected


def test_PD004_fail():
    """
    Test that using .notnull() results in an error.
    """
    statement = "notnulls = pd.notnull(val)"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = [PD004(1, 11)]
    assert actual == expected
