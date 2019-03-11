"""
Test to check for `.merge()` method on pandas root object.

Although the `.merge()` method is defined for both the pandas root object
(`pd.merge()`) and the pandas DataFrame object (`df.merge()`), the preferred
syntax is to use the DataFrame.  
"""
import ast

from pandas_vet import VetPlugin
from pandas_vet import PD015


def test_PD015_pass_merge_on_dataframe():
    """
    Test that using .merge() on the dataframe does not result in an error.
    """
    pass    ### NOT YET IMPLEMENTED
    statement = "df.method( XXX )"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = []
    assert actual == expected


def test_PD015_fail_merge_on_pandas_object():
    """
    Test that using .merge() on the pandas root object generates an error.
    """
    pass    ### NOT YET IMPLEMENTED
    statement = "pd.method( XXX )"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = [PD015(1, 0)]
    assert actual == expected
