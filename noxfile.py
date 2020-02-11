import nox


SOURCES = "pandas_vet setup.py tests --exclude tests/data".split()


@nox.session
def lint(session):
    session.install("-r", "reqs/lint.txt")
    session.run("flake8", *SOURCES)
    session.run("black", "--check", *SOURCES)


@nox.session
def test(session):
    session.install("-r", "reqs/test.txt")
    # TODO: ensuring that local vet environment is setup ( pip install -e)
    session.run("pytest", "--cov=pandas_vet")
    session.run("flake8", "pandas_vet", "setup.py", "tests",
                "--exclude tests/data")
    # TODO: session.run black
    # black --check pandas_vet setup.py tests --exclude tests/data


@nox.session
def install_vet_dev_mode(session):
    """Install pandas-vet development mode"""
    pass
