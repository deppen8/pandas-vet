from collections import namedtuple
from functools import partial


class VetPlugin:
    name = "flake8-pandas-vet"
    version = "0.1.0"

    def __init__(self, tree):
        self.tree = tree

    def run(self):
        for message in []:
            yield message


error = namedtuple("Error", ["lineno", "col", "message", "type"])
Error = partial(partial, error, type=VetPlugin)


PD001 = Error(
    "pandas should always be imported as 'import pandas as pd'"
)
PD002 = Error(
    "'inplace = True' should be avoided; it has inconsistent behavior"
)
PD003 = Error(
    "'.isna' is preferred to '.isnull'; functionality is equivalent"
)
PD004 = Error(
    "'.notna' is preferred to '.notnull'; functionality is equivalent"
)
PD005 = Error(
    "Use arithmetic operator instead of method"
)
PD006 = Error(
    "Use comparison operator instead of method"
)
