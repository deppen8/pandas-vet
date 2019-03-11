"""
Test to check for use of the pandas dataframe `.array` attribute
or `.to_array()` method in preference to `.values` attribute.
"""
import ast

from pandas_vet import VetPlugin
from pandas_vet import PD011


def test_PD011_pass_to_array():
    """
    Test that using .to_array() explicitly does not result in an error.
    """
    statement = "result = df.to_array()"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = []
    assert actual == expected


def test_PD011_pass_array():
    """
    Test that using .array explicitly does not result in an error.
    """
    statement = "result = df.array"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = []
    assert actual == expected


def test_PD011_fail_values():
    """
    Test that using .values data frame attribute results in an error.
    """
    statement = "result = df.values"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = [PD011(1, 9)]
    assert actual == expected


def test_PD011_pass_node_Name():
    """
    Test that where 'values' is a Name does NOT raise an error
    """
    statement = "result = values"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = []
    assert actual == expected
