# stdlib
import ast

from pandas_vet import VetPlugin
from pandas_vet import PD003


def test_PD003_pass():
    """
    Test that using .isna() explicitly does not result in an error.
    """
    statement = "nas = pd.isna(val)"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = []
    assert actual == expected


def test_PD003_fail():
    """
    Test that using .isnull() results in an error.
    """
    statement = "nulls = pd.isnull(val)"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = [PD003(1, 8)]
    assert actual == expected


