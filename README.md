# pandas-vet

![tests](https://github.com/deppen8/pandas-vet/workflows/Lint%20and%20test/badge.svg
)
[![codecov](https://codecov.io/gh/deppen8/pandas-vet/branch/master/graph/badge.svg?token=VgpjplhNr0)](https://codecov.io/gh/deppen8/pandas-vet)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PyPI - License](https://img.shields.io/pypi/l/pandas-vet.svg)](https://github.com/deppen8/pandas-vet/blob/master/LICENSE)

[![PyPI](https://img.shields.io/pypi/v/pandas-vet.svg)](https://pypi.org/project/pandas-vet/)
[![PyPI - Status](https://img.shields.io/pypi/status/pandas-vet.svg)](https://pypi.org/project/pandas-vet/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/pandas-vet.svg)](https://pypi.org/project/pandas-vet/)

[![Conda Version](https://img.shields.io/conda/vn/conda-forge/pandas-vet.svg)](https://anaconda.org/conda-forge/pandas-vet)
[![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/pandas-vet.svg)](https://anaconda.org/conda-forge/pandas-vet)

`pandas-vet` is a plugin for `flake8` that provides opinionated linting for `pandas` code.

It began as a project during the PyCascades 2019 sprints.

## Motivation

Starting with `pandas` can be daunting. The usual internet help sites are littered with different ways to do the same thing and some features that the `pandas` docs themselves discourage live on in the API. `pandas-vet` is (hopefully) a way to help make `pandas` a little more friendly for newcomers by taking some opinionated stances about `pandas` best practices. It is designed to help users reduce the `pandas` universe.

The idea to create a linter was sparked by [Ania Kapuścińska](https://twitter.com/lambdanis)'s talk at PyCascades 2019, ["Lint your code responsibly!"](https://youtu.be/hAnCiTpxXPg?t=21814).

Many of the opinions stem from [Ted Petrou's](https://twitter.com/TedPetrou) excellent [Minimally Sufficient Pandas](https://medium.com/dunder-data/minimally-sufficient-pandas-a8e67f2a2428). Other ideas are drawn from `pandas` docs or elsewhere. The [Pandas in Black and White](https://deppen8.github.io/pandas-bw/) flashcards have a lot of the same opinions too.

## Installation

`pandas-vet` is a plugin for `flake8`. If you don't have `flake8` already, it will install automatically when you install `pandas-vet`.

The plugin is on PyPI and can be installed with:

```bash
pip install pandas-vet
```

It can also be installed with `conda`:

```bash
conda install -c conda-forge pandas-vet
```

`pandas-vet` is tested under Python 3.6, 3.7, 3.8, and 3.9 as defined in our [GitHub Actions](https://github.com/deppen8/pandas-vet/blob/master/.github/workflows/testing.yml)

## Usage

Once installed successfully in an environment that also has `flake8` installed, `pandas-vet` should run whenever `flake8` is run.

```bash
$ flake8 ...
```

See the [`flake8` docs](http://flake8.pycqa.org/en/latest/user/invocation.html) for more information.

For a full list of implemented warnings, see [the list below](#list-of-warnings).

## Contributing

`pandas-vet` is still in the very early stages. Contributions are welcome from the community on code, tests, docs, and just about anything else.

### Code of Conduct

Because this project started during the PyCascades 2019 sprints, we adopt the PyCascades minimal expectation that we "Be excellent to each another". Beyond that, we follow the Python Software Foundation's [Community Code of Conduct](https://www.python.org/psf/codeofconduct/).

### Steps to contributing

1. Please submit an issue (or draft PR) first describing the types of changes you'd like to implement.

2. Fork the repo and create a new branch for your enhancement/fix.

3. Get a development environment set up with your favorite environment manager (`conda`, `virtualenv`, etc.).

    0. You must use at least python 3.6 to develop, for [black](https://github.com/psf/black) support.

    1. You can create one from `pip install -r requirements_dev.txt` or, if you use Docker, you can build an image from the Dockerfile included in this repo.

    2. Once your enviroment is set up you will need to install pandas-vet in development mode. Use `pip install -e .` (use this if you are alreay in your virtual enviroment) or `pip install -e <path>` (use this one if not in the virtual enviroment and prefer to state explicitly where it is going).


4. Write code, docs, etc.

5. We use `pytest`, `flake8`, and `black` to validate our codebase. TravisCI integration will complain on pull requests if there are any failing tests or lint violations. To check these locally, run the following commands:

```bash
pytest --cov="pandas_vet"
```

```bash
flake8 pandas_vet setup.py tests --exclude tests/data
```

```bash
black --check pandas_vet setup.py tests --exclude tests/data
```



6. Push to your forked repo.

7. Submit pull request to the parent repo from your branch. Be sure to write a clear message and reference the Issue # that relates to your pull request.

8. Feel good about giving back to open source projects.

### How to add a check to the linter

1. Write tests. At a *minimum*, you should have test cases where the linter should catch "bad" `pandas` and test cases where the linter should allow "good" `pandas`.

2. Write your check function in `/pandas-vet/__init__.py`.

3. Run `flake8` and `pytest` on the linter itself (see [Steps to contributing](#steps-to-contributing))


## Contributors

### PyCascades 2019 sprints team

- Sam Beck
- [Jacob Deppen](https://twitter.com/jacob_deppen)
- [Walt](https://github.com/wadells)
- Charles Simchick
- [Aly Sivji](https://twitter.com/CaiusSivjus)
- Tim Smith

### PyCascades 2020 sprints team

- dat-boris
- [Jacob Deppen](https://twitter.com/jacob_deppen)
- jvano74
- keturn
- Rhornberger
- tojo13
- [Walt](https://github.com/wadells)

### Other awesome contributors

- Earl Clark
- Leandro Leites
- pwoolvett
- sigmavirus24

## List of warnings

**PD001:** pandas should always be imported as 'import pandas as pd'

**PD002:** 'inplace = True' should be avoided; it has inconsistent behavior

**PD003:** '.isna' is preferred to '.isnull'; functionality is equivalent

**PD004:** '.notna' is preferred to '.notnull'; functionality is equivalent

**PD005:** Use arithmetic operator instead of method

**PD006:** Use comparison operator instead of method

**PD007:** '.ix' is deprecated; use more explicit '.loc' or '.iloc'

**PD008:** Use '.loc' instead of '.at'.  If speed is important, use numpy.

**PD009:** Use '.iloc' instead of '.iat'.  If speed is important, use numpy.

**PD010** '.pivot_table' is preferred to '.pivot' or '.unstack'; provides same functionality

**PD011** Use '.array' or '.to_array()' instead of '.values'; 'values' is ambiguous

**PDO12** '.read_csv' is preferred to '.read_table'; provides same functionality

**PD013** '.melt' is preferred to '.stack'; provides same functionality

**PD015** Use '.merge' method instead of 'pd.merge' function. They have equivalent functionality.

### *Very* Opinionated Warnings

These warnings are turned off by default. To enable them, add the `-annoy` flag to your command, e.g.,

```bash
$ flake8 --annoy my_file.py
```

**PD901** 'df' is a bad variable name. Be kinder to your future self.
