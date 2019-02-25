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
