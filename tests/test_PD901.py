import ast

from pandas_vet import PD901, VetPlugin


def test_PD901_pass_non_df():
    statement = "employees = pd.DataFrame(employee_dict)"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = []
    assert actual == expected


def test_PD901_pass_part_df():
    statement = "employees_df = pd.DataFrame(employee_dict)"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = []
    assert actual == expected


def test_PD901_pass_df_param():
    statement = "my_function(df=data)"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = []
    assert actual == expected


def test_PD901_fail_df_var():
    statement = "df = pd.DataFrame()"
    tree = ast.parse(statement)
    actual = list(VetPlugin(tree).run())
    expected = [PD901(1, 0)]
    assert actual == expected
