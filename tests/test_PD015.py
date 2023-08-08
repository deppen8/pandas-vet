"""
Test to check for `.merge()` method on pandas root object.

Although the `.merge()` method is defined for both the pandas root object
and the pandas DataFrame object, the preferred syntax is to use the DataFrame.

The only difference in the methods is that for the pandas root method, an
additional positional parameter is required to specify the dataframe to be
merged.  The methods are differentiated in the AST by comparing the type
of the base object.  A definitive distinction between these methods must
check the type of the base object.

    pd.merge(left, right, how='inner', on=None, ... )
    df.merge(right, how='inner', on=None, ... )
"""
import ast

from pandas_vet import PD015, VetPlugin


def test_PD015_pass_merge_on_dataframe():
    """
    Test that using .merge() on the dataframe does not result in an error.
    """
    statement = "df1.merge(df2)"
    tree = ast.parse(statement)
    expected = []
    actual = list(VetPlugin(tree).run())
    assert actual == expected


def test_PD015_pass_merge_on_dataframe_with_multiple_args():
    """
    Test that using `df.merge(arg1, arg2)` does not produce an error.
    """
    statement = "df1.merge(df2, 'inner')"
    tree = ast.parse(statement)
    expected = []
    actual = list(VetPlugin(tree).run())
    assert actual == expected


def test_PD015_fail_merge_on_pandas_object():
    """
    Test that using .merge() on the pandas root object generates an error.
    """
    statement = "pd.merge(df1, df2)"
    tree = ast.parse(statement)
    expected = [PD015(1, 0)]
    actual = list(VetPlugin(tree).run())
    assert actual == expected


def test_PD015_pass_merge_no_id_func_value():
    statement = "pd.to_datetime(timestamp * 10 ** 9).strftime('%Y-%m-%d %H:%M:%S.%f')"
    tree = ast.parse(statement)
    expected = []
    actual = list(VetPlugin(tree).run())
    assert actual == expected
