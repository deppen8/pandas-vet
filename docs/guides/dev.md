# Development

Contributions are welcome from the community on code, tests, docs, and just about anything else.

## Code of Conduct

Because this project started during the PyCascades 2019 sprints, we adopt the PyCascades minimal expectation that we "Be excellent to each another". Beyond that, we follow the Python Software Foundation's [Community Code of Conduct](https://www.python.org/psf/codeofconduct/).

## Project management

We use [Hatch](https://hatch.pypa.io/) for project management. This includes:

- A package build system.
- Easy version bumping.
- Running scripts (e.g., tests, formatting, docs).

The best way to install Hatch on your machine is to use [`pipx`](https://pipxproject.github.io/pipx/).

```bash
pipx install hatch
```

## Contribution workflow

1. Please submit an [Issue](https://github.com/deppen8/pandas-vet/issues) (or draft PR) first describing the types of changes you'd like to implement.

2. Fork the GitHub repository.

3. Create a new branch for your enhancement/fix.

4. Write code, [tests](tests), [docs](documentation), etc. See [How to add a check to the linter](linter-check).

5. We use `pytest`, `flake8`, `isort`, and `black` to test, lint, and format our codebase. You can invoke these with a single Hatch command from the root of the repository.

    ```bash
    hatch run dev:tests
    ```

    This command will build the necessary virtual environments, install the package in editable mode, and run the tests, linting, and formatting checks.

    These are the same commands that are run in the CI/CD pipeline. See the [Tests](tests) section below for more details.

6. Push your branch to your forked repository.

7. Submit a pull request to the parent repository from your branch. Be sure to write a clear message and reference any Issue # that relates to your pull request.

8. Feel good about giving back to open source projects.

(linter-check)=

## How to add a check to the linter

1. Write tests. At a *minimum*, you should have test cases where the linter should catch "bad" `pandas` and test cases where the linter should allow "good" `pandas`.

2. Write your check function in `/pandas-vet/__init__.py`.

3. Run `hatch run dev:tests` and fix any errors.

## Custom scripts

In addition to the `tests` script used in CI/CD, we have a few predefined scripts that are useful for development. These are defined in the `pyproject.toml` file and can be run with `hatch run dev:<script_name>`. For example, to run a combination of `isort`, `black`, and `flake8` you can run:

```bash
hatch run dev:format
```

The available custom scripts are:

- `check` - Run `isort`, `black`, and `flake8` without making changes (i.e., a dry-run).
- `format` - Run `isort`, `black`, and `flake8`.
- `tests` - Run the test suite and format.
- `docs` - Build the docs with Jupyter Book.

(tests)=

## Tests

We use `pytest` for testing. Tests live in the `/tests` directory. The use of [`pytest` fixtures](https://docs.pytest.org/en/stable/explanation/fixtures.html) is encouraged and these should typically be stored in `/tests/conftest.py`, though in some limited cases could be isolated to a particular test module.

Use `hatch run dev:tests` to run the test suite. This will also run static linting with `flake8`, and reformatting with `black` and `isort`. All of these must "pass" for the tests to be considered fully passing.

````{tip}
When `pytest` is run, it will also run a `coverage` report. This can be used as a rough guide to where test coverage is missing, though it is by no means a measure of the quality of your tests.

```bash
----------- coverage: platform linux, python 3.9.9-final-0 -----------
Name                             Stmts   Miss  Cover   Missing
--------------------------------------------------------------
pandas_vet/__init__.py       1      0   100%
pandas_vet/utils.py         38      1    97%   98
--------------------------------------------------------------
TOTAL                               39      1    97%
Coverage HTML written to dir results/cov_html
Coverage XML written to file results/coverage.xml
```
````

(documentation)=

## Documentation

The documentation is built with a combination of docstrings in Google docstring format and Jupyter Book deployment. Jupyter Book provides an easy way to combine traditional API docs built with Sphinx, Markdown docs like this page, and Jupyter Notebook guides/tutorials.

### Docstrings

Docstrings should use the [Google docstring style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html). Each class and function should have a docstring.

When the docs are built with Jupyter Book, Sphinx will detect the docstrings and turn them into some nicely-formatted API docs.

### Jupyter Book

[Jupyter Book](https://jupyterbook.org/intro.html) provides the engine for the docs. Documentation pages can be written in reStructuredText, Markdown, or Jupyter Notebooks. See the [Jupyter Book documentation](https://jupyterbook.org/intro.html) for additional features available.

### Build the docs locally

The docs are built and deployed to GitLab Pages as part of the CI/CD pipeline in GitLab. However, if you'd like to examine them locally, you can build them yourself with `hatch run dev:docs`, e.g.,

```console
$ hatch run dev:docs

--------------------------------------------------------------------------------
building JupyterBook documentation
--------------------------------------------------------------------------------
Installing dependencies from lock file

No dependencies to install or update

Installing the current project: pandas_vet (0.0.1)
Running Jupyter-Book v0.12.1
Source Folder: /app/docs
Config Path: /app/docs/_config.yml
Output Path: /app/docs/_build/html
Running Sphinx v4.4.0
loading pickled environment... done
myst v0.15.2: MdParserConfig(renderer='sphinx', commonmark_only=False, enable_extensions=['colon_fence', 'dollarmath', 'linkify', 'substitution', 'tasklist'], dmath_allow_labels=True, dmath_allow_space=True, dmath_allow_digits=True, dmath_double_inline=False, update_mathjax=True, mathjax_classes='tex2jax_process|mathjax_process|math|output_area', disable_syntax=[], url_schemes=['mailto', 'http', 'https'], heading_anchors=None, heading_slug_func=None, html_meta=[], footnote_transition=True, substitutions=[], sub_delimiters=['{', '}'], words_per_minute=200)
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 1 source files that are out of date
updating environment: 0 added, 1 changed, 0 removed
reading sources... [100%] dev
looking for now-outdated files... none found
pickling environment... done
checking consistency... done
preparing documents... done
writing output... [100%] index
/app/docs/dev.md:1: WARNING: Could not lex literal_block as "bash". Highlighting skipped.
generating indices... genindex py-modindex done
highlighting module code... [100%] pandas_vet.tile
writing additional pages... search done
copying static files... done
copying extra files... done
dumping search index in English (code: en)... done
dumping object inventory... done
build succeeded, 1 warning.

The HTML pages are in docs/_build/html.

===============================================================================

Finished generating HTML for book.
Your book's HTML pages are here:
    docs/_build/html/
You can look at your book by opening this file in a browser:
    docs/_build/html/index.html
Or paste this line directly into your browser bar:
    file:///app/docs/_build/html/index.html

===============================================================================
```

Any errors in the build will be logged as part of this output.

## CI/CD

CI/CD is handled by GitHub Actions. Configuration can be found in the `.github/workflows/` folder.

When a pull request is submitted, the code is tested, linted, and formatted (`hatch run dev:tests`) and the docs are built (`hatch run dev:docs`). If any of these steps fail, the pull request will be marked as failing.

When a pull request is merged into the `main` branch, the code is tested, linted, and formatted (`hatch run dev:tests`), the docs are built (`hatch run dev:docs`), and the docs are deployed to GitHub Pages.
