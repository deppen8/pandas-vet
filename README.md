# pandas-vet

[![Build Status](https://travis-ci.org/deppen8/pandas-vet.svg?branch=master)](https://travis-ci.org/deppen8/pandas-vet)
[![PyPI - Status](https://img.shields.io/pypi/status/pandas-vet.svg)](https://pypi.org/project/pandas-vet/)
[![PyPI](https://img.shields.io/pypi/v/pandas-vet.svg)](https://pypi.org/project/pandas-vet/)
[![PyPI - License](https://img.shields.io/pypi/l/pandas-vet.svg)](https://github.com/deppen8/pandas-vet/blob/master/LICENSE)

`pandas-vet` is a plugin for `flake8` that provides opinionated linting for `pandas` code.

It began as a project during the PyCascades 2019 sprints.

## Motivation

Starting with `pandas` can be daunting. The usual internet help sites are littered with different ways to do the same thing and some features that the `pandas` docs themselves discourage live on in the API. `pandas-vet` is (hopefully) a way to help make `pandas` a little more friendly for newcomers by taking some opinionated stances about `pandas` best practices. It is designed to help users reduce the `pandas` universe.

The idea to create a linter was sparked by [Ania Kapuścińska](https://twitter.com/lambdanis)'s talk at PyCascades 2019, ["Lint your code responsibly!"](https://youtu.be/hAnCiTpxXPg?t=21814).

Many of the opinions stem from [Ted Petrou's](https://twitter.com/TedPetrou) excellent [Minimally Sufficient Pandas](https://medium.com/dunder-data/minimally-sufficient-pandas-a8e67f2a2428). Other ideas are drawn from `pandas` docs or elsewhere. The [Pandas in Black and White](https://deppen8.github.io/pandas-bw/) flashcards have a lot of the same opinions too.

## Installation

`pandas-vet` is a plugin for `flake8`. If you don't have `flake8` already, it will install automatically when you install `pandas-vet`.

## Usage

Once installed successfully in an environment that also has `flake8` installed, `pandas-vet` should run whenever `flake8` is run.

```bash
$ flake8 ...
```

See the [`flake8` docs](http://flake8.pycqa.org/en/latest/user/invocation.html) for more information.

## Contributing

`pandas-vet` is still in the very early stages. Contributions are welcome from the community on code, tests, docs, and just about anything else.

### Steps to contributing

1. Please submit an issue (or draft PR) first describing the types of changes you'd like to implement.

2. Fork the repo and create a new branch for your enhancement/fix.

3. Write code, docs, etc.

4. We use `pytest` and `flake8` to validate our codebase. The TravisCI integration will complain on pull requests if there are any failing tests or lint violations. To check these locally, run the following commands:

```bash
pytest tests
```

```bash
flake8 pandas_vet setup.py tests --exclude tests/data
```

5. Push to your forked repo.

6. Submit pull request to the parent repo from your branch. Be sure to write a clear message and reference the Issue # that relates to your pull request.

7. Feel good about giving back to open source projects.

### How to add a check to the linter

1. Write tests. At a *minimum*, you should have test cases where the linter should catch "bad" `pandas` and test cases where the linter should allow "good" `pandas`.

2. Write your check function in `/pandas-vet/__init__.py`.

3. Run `flake8` and `pytest` on the linter itself (see [Steps to contributing](#steps-to-contributing))

### Code of Conduct

Because this project started during the PyCascades 2019 sprints, we adopt the PyCascades minimal expectation that we "Be excellent to each another". Beyond that, we follow the Python Software Foundation's [Community Code of Conduct](https://www.python.org/psf/codeofconduct/).

## Contributors

### PyCascades 2019 sprints team

- Sam Beck
- [Jacob Deppen](https://twitter.com/jacob_deppen)
- Walt Javins
- Charles Simchick
- [Aly Sivji](https://twitter.com/CaiusSivjus)
- Tim Smith
