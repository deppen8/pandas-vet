# pandas-vet

`pandas-vet` is a plugin for `flake8` that provides opinionated linting for `pandas` code.

[![Documentation Status](https://readthedocs.org/projects/pandas-vet/badge/?version=stable)](https://pandas-vet.readthedocs.io/en/latest/?badge=stable)

[![Test and lint](https://github.com/deppen8/pandas-vet/actions/workflows/testing.yml/badge.svg)](https://github.com/deppen8/pandas-vet/actions/workflows/testing.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PyPI - License](https://img.shields.io/pypi/l/pandas-vet.svg)](https://github.com/deppen8/pandas-vet/blob/main/LICENSE)

[![PyPI](https://img.shields.io/pypi/v/pandas-vet.svg)](https://pypi.org/project/pandas-vet/)
[![PyPI - Status](https://img.shields.io/pypi/status/pandas-vet.svg)](https://pypi.org/project/pandas-vet/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/pandas-vet.svg)](https://pypi.org/project/pandas-vet/)

[![Conda Version](https://img.shields.io/conda/vn/conda-forge/pandas-vet.svg)](https://anaconda.org/conda-forge/pandas-vet)
[![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/pandas-vet.svg)](https://anaconda.org/conda-forge/pandas-vet)

## Basic usage

Take the following script, `drop_column.py`, which contains valid pandas code:

```python
# drop_column.py
import pandas

df = pandas.DataFrame({
    'col_a': [i for i in range(20)],
    'col_b': [j for j in range(20, 40)]
})
df.drop(columns='col_b', inplace=True)
```

With `pandas-vet` installed, if we run Flake8 on this script, we will see three warnings raised.

```bash
$ flake8 drop_column.py

./drop_column.py:2:1: PD001 pandas should always be imported as 'import pandas as pd'
./drop_column.py:4:1: PD901 'df' is a bad variable name. Be kinder to your future self.
./drop_column.py:7:1: PD002 'inplace = True' should be avoided; it has inconsistent behavior
```

We can use these to improve the code.

```python
# pandastic_drop_column.py
import pandas as pd

ab_dataset = pd.DataFrame({
    'col_a': [i for i in range(20)],
    'col_b': [j for j in range(20, 40)]
})
a_dataset = ab_dataset.drop(columns='col_b')
```

For a full list, see the [Supported warnings](https://deppen8.github.io/pandas-vet/guides/warnings.html) page of the documentation.

## Motivation

Starting with [pandas](https://pandas.pydata.org/) can be daunting. The usual internet help sites are littered with different ways to do the same thing and some features that the pandas docs themselves discourage live on in the API. `pandas-vet` is (hopefully) a way to help make pandas a little more friendly for newcomers by taking some opinionated stances about pandas best practices. It is designed to help users reduce the pandas universe.

The idea to create a linter was sparked by [Ania Kapuścińska](https://twitter.com/lambdanis)'s talk at PyCascades 2019, ["Lint your code responsibly!"](https://youtu.be/hAnCiTpxXPg?t=21814). The package was largely developed at the PyCascades 2019 sprints.

Many of the opinions stem from [Ted Petrou's](https://twitter.com/TedPetrou) excellent [Minimally Sufficient Pandas](https://medium.com/dunder-data/minimally-sufficient-pandas-a8e67f2a2428). Other ideas are drawn from pandas docs or elsewhere. The [Pandas in Black and White](https://deppen8.github.io/pandas-bw/) flashcards have a lot of the same opinions too.
