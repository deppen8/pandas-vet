"""
Test to check functionality for use of the `.melt()` data frame
method in preference to `.stack()` method.
"""
import ast

from pandas_vet import VetPlugin
from pandas_vet import PD013


def test_PD013_pass():
    """
    Test that using .melt() explicitly does not result in an error.
    """
    statement = """table = df.melt(
        id_vars='airline',
        value_vars=['ATL', 'DEN', 'DFW'],
        value_name='airline delay'
        )
    """
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = []
    assert actual == expected


def test_PD013_fail_stack():
    """
    Test that using .stack() results in an error.
    """
    statement = "table = df.stack(level=-1, dropna=True)"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = [PD013(1, 8)]
    assert actual == expected
