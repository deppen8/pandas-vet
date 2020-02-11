import nox


# TODO: set multiple versions
# see docs at https://github.com/payscale/fables/blob/master/noxfile.py
# py_versions = ["3.8", "3.7", "3.6"]
SOURCES = "pandas_vet setup.py noxfile.py tests --exclude tests/data".split()


#
@nox.session(reuse_venv=True)
def blacken(session):
    session.install("-r", "reqs/lint.txt")
    session.run("black", *SOURCES)


@nox.session(reuse_venv=True)
def lint(session):
    session.install("-r", "reqs/lint.txt")
    session.run("flake8", *SOURCES, "")
    session.run("black", "--check", *SOURCES)


@nox.session(reuse_venv=True)
def test(session):
    session.install("-r", "reqs/test.txt")
    session.install("-e", ".")
    session.run("pytest", "--cov=pandas_vet")
