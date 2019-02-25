# stdlib
import ast

from pandas_vet import VetPlugin
from pandas_vet import PD001, PD002, PD003, PD004


def test_PD001_pass():
    """
    Test that importing pandas the recommended way does not result in an error.
    """
    statement = "import pandas as pd"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = []
    assert actual == expected


def test_PD001_fail_no_as():
    """
    Test that importing pandas without an 'as' clause results in an error.
    """
    statement = "import pandas"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = [PD001(1, 0)]
    assert actual == expected


def test_PD001_fail_wrong_alias():
    """
    Test that importing pandas with an odd name results in an error.
    """
    statement = "import pandas as foo"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = [PD001(1, 0)]
    assert actual == expected


def test_PD002_pass():
    """
    Test that using inplace=False explicitly does not result in an error.
    """
    statement = """df.drop(['a'], axis=1, inplace=False)"""
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = []
    assert actual == expected


def test_PD002_fail():
    """
    Test that using inplace=True results in an error.
    """
    statement = """df.drop(['a'], axis=1, inplace=True)"""
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = [PD002(1, 0)]
    assert actual == expected


def test_PD003_pass():
    """
    Test that using .isna() explicitly does not result in an error.
    """
    statement = "if pd.isna():"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = []
    assert actual == expected


def test_PD003_fail():
    """
    Test that using .isnull() results in an error.
    """
    statement = "if pd.isnull():"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = [PD003(1, 0)]
    assert actual == expected


def test_PD004_pass():
    """
    Test that using .notna() explicitly does not result in an error.
    """
    statement = "if pd.notna():"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = []
    assert actual == expected


def test_PD004_fail():
    """
    Test that using .notnull() results in an error.
    """
    statement = "if pd.notnull():"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = [PD004(1, 0)]
    assert actual == expected


