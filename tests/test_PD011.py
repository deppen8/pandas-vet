"""
Test to check for use of the pandas dataframe `.to_numpy()` method in preference to `.values` attribute.
"""
import ast

from pandas_vet import PD011, VetPlugin


def test_PD011_pass_to_numpy():
    """
    Test that using .to_numpy() explicitly does not result in an error.
    """
    statement = "result = df.to_numpy()"
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


def test_PD011_pass_values_call():
    """
    Test that using .values() attribute call does not result in an error.
    """
    statement = "result = {}.values()"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = []
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
