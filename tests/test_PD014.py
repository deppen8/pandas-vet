"""
Test to check for use of the slicing syntax with `.groupby()` method

### 2019.03.07 TESTS DON'T YET EXIST FOR ALL OF THESE PATTERNS

Valid (?) patterns for `.groupby()` method:
    groupby('group_col')
    groupby('group_col').agg('agg_col')
    groupby('group_col').agg('agg_func')
    groupby('group_col').agg({'agg_col': 'agg_func'})
    df.groupby('group_col')
    df.groupby('group_col').agg('agg_col')
    df.groupby('group_col').agg('agg_func')
    df.groupby('group_col').agg({'agg_col': 'agg_func'})

Invalid patterns for `.groupby()` method:
    groupby('group_col')['agg_col']
    groupby('group_col')['agg_col'].agg('agg_func')
    groupby('group_col')['agg_col'].agg_func()
    df.groupby('group_col')['agg_col']
    df.groupby('group_col')['agg_col'].agg('agg_func')
    df.groupby('group_col')['agg_col'].agg_func()

NOTE:
    For method  calls, function name is in node.value.func.attr

### 2019.03.07 IS THERE VALID SYNTAX FOR A `groupby()` FUNCTION CALL ?

Valid (?) patterns for `groupby()` function:
    groupby('group_col')
    groupby('group_col').agg('agg_col')
    groupby('group_col').agg('agg_func')
    groupby('group_col').agg({'agg_col': 'agg_func'})

Invalid patterns for `groupby()` function:
    groupby('group_col')['agg_col']
    groupby('group_col')['agg_col'].agg('agg_func')
    groupby('group_col')['agg_col'].agg_func()

NOTE:
    For function calls, function name is in node.value.func.id
"""
import ast

from pandas_vet import VetPlugin
from pandas_vet import PD014


def test_PD014_pass_groupby_method_with_no_slicing():
    """
    Test that using .groupby() without slicing does not result in an error.
    """
    statement = "df.groupby('group_col')"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = []
    assert actual == expected


def test_pd014_pass_groupby_method_with_no_slicing_with_agg_method():
    """
    test that using .groupby().agg() without slicing does not result in an error.
    """
    statement = "df.groupby('group_col').agg('agg_func')"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = []
    assert actual == expected


def test_PD014_pass_groupby_method_with_no_slicing_with_agg_columns():
    """
    Test that using .groupby().agg() without slicing does not result in an error.
    """
    statement = "df.groupby('group_col').agg({'agg_col': 'agg_func'})"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = []
    assert actual == expected


def test_PD014_fail_groupby_method_with_slicing():
    """
    Test that using .groupby()[] syntax results in an error.
    """
    statement = "df.groupby('group_col')['agg_col']"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = [PD014(1, 0)]
    assert actual == expected


def test_PD014_fail_groupby_method_with_slicing_and_agg_method():
    """
    Test that using .groupby()[].agg() syntax results in an error.
    """
    statement = "df.groupby('group_col')['agg_col'].agg('agg_func')"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = [PD014(1, 0)]
    assert actual == expected


def test_PD014_fail_groupby_method_with_slicing_and_agg_func():
    """
    test that using .groupby()[].agg_func() syntax results in an error.
    """
    statement = "df.groupby('group_col')['agg_col'].agg_func()"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = [PD014(1, 0)]
    assert actual == expected


## Below functions test for use of `groupby() function, independent of dataframe
## DOES THIS MAKE ANY SENSE?
#
#def test_PD014_pass_groupby_function_with_no_slicing():
#    """
#    Test that using groupby() without slicing does not result in an error.
#    """
#    statement = "groupby('group_col')"
#    tree = ast.parse(statement)
#    actual = list(VetPlugin(tree).run())
#    expected = []
#    assert actual == expected
#
#
#def test_PD014_pass_groupby_function_with_no_slicing_with_agg_method():
#    """
#    Test that using groupby().agg() without slicing does not result in an error.
#    """
#    statement = "groupby('group_col').agg('agg_func')"
#    tree = ast.parse(statement)
#    actual = list(VetPlugin(tree).run())
#    expected = []
#    assert actual == expected
#
#
#def test_PD014_pass_groupby_function_with_no_slicing_with_agg_columns():
#    """
#    Test that using groupby().agg() without slicing does not result in an error.
#    """
#    statement = "groupby('group_col').agg({'agg_col': 'agg_func'})"
#    tree = ast.parse(statement)
#    actual = list(VetPlugin(tree).run())
#    expected = []
#    assert actual == expected
#
#
#def test_PD014_fail_groupby_function_with_slicing():
#    """
#    Test that using groupby()[] syntax results in an error.
#    """
#    statement = "groupby('group_col')['agg_col']"
#    tree = ast.parse(statement)
#    actual = list(VetPlugin(tree).run())
#    expected = [PD014(1, 0)]
#    assert actual == expected
#
#
#def test_PD014_fail_groupby_function_with_slicing_and_agg_method():
#    """
#    Test that using groupby()[].agg() syntax results in an error.
#    """
#    statement = "groupby('group_col')['agg_col'].agg('agg_func')"
#    tree = ast.parse(statement)
#    actual = list(VetPlugin(tree).run())
#    expected = [PD014(1, 0)]
#    assert actual == expected
#
#
#def test_PD014_fail_groupby_function_with_slicing_and_agg_func():
#    """
#    test that using groupby()[].agg_func() syntax results in an error.
#    """
#    statement = "groupby('group_col')['agg_col'].agg_func()"
#    tree = ast.parse(statement)
#    actual = list(VetPlugin(tree).run())
#    expected = [PD014(1, 0)]
#    assert actual == expected
