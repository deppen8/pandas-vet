"""
Test to check functionality for use of the `.pivot_table()` data frame
method in preference to either `.pivot()` or `.unstack()` methods.  
"""
import ast

from pandas_vet import VetPlugin
from pandas_vet import PD010


def test_PD010_pass():
    """
    Test that using .pivot_table() explicitly does not result in an error.
    """
    statement = "table = df.pivot_table(df, values='D', index=['A', 'B'], columns=['C'], aggfunc=np.sum, fill_value=0)"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = []
    assert actual == expected


def test_PD010_fail_pivot():
    """
    Test that using either pd.pivot(df) or df.pivot() methods results in an error.
    """
    statement = "table = pd.pivot(df, index='foo', columns='bar', values='baz')"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = [PD010(1, 8)]
    assert actual == expected


def test_PD010_fail_unstack():
    """
    Test that using .unstack() results in an error.
    """
    statement = "table = df.unstack(level=0)"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = [PD010(1, 8)]
    assert actual == expected
