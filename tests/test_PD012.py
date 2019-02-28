"""
Test to check for use of the pandas dataframe soon-to-be-deprecated 
`.read_table()` method. 
"""
import ast

from pandas_vet import VetPlugin
from pandas_vet import PD012


def test_PD012_pass_read_csv():
    """
    Test that using .read_csv() explicitly does not result in an error.
    """
    statement = "df = pd.read_csv(input_file)"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = []
    assert actual == expected


def test_PD012_fail_read_table():
    """
    Test that using .read_table() method results in an error.
    """
    statement = "df = pd.read_table(input_file)"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = [PD012(1, 5)]
    assert actual == expected


