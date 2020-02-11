# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os.path

_pandas_vet_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "pandas_vet")
)
# import sys
# sys.path.insert(0, _pandas_vet_path)


# -- Project information -----------------------------------------------------

project = "pandas-vet"
copyright = "2020, Jacob Deppen"
author = "Jacob Deppen"


def _pandas_vet_version():
    version = {}
    with open(os.path.join(_pandas_vet_path, "version.py")) as fp:
        # exec? well, it's what our setup.py does.
        exec(fp.read(), version)
    return version["__version__"]


# The full version, including alpha/beta/rc tags
release = _pandas_vet_version()


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["sphinx.ext.todo", "autoapi.extension", "sphinx_rtd_theme"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Warn about all references where the target cannot be found.
# nitpicky = True

# Aliases for some commonly-used phrases so they're styled consistently.
rst_epilog = """
.. |flake8| replace:: ``flake8``
.. |pandas| replace:: ``pandas``
.. |pandas-vet| replace:: ``pandas-vet``
"""

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


# -- Extension configuration -------------------------------------------------

autoapi_dirs = [_pandas_vet_path]

# There's only one module, so we'll link directly to it insead of autoapi/index.
autoapi_add_toctree_entry = False

todo_include_todos = True
todo_emit_warnings = True
