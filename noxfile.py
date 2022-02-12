import nox


@nox.session
def format(session: nox.Session) -> None:
    session.install("black", "isort")
    session.run("isort", ".")
    session.run("black", ".")


@nox.session
def lint(session: nox.Session) -> None:
    session.install("flakeheaven", "flake8-annotations", "flake8-docstrings")
    session.run("flakeheaven", "lint")


@nox.session
def mypy(session: nox.Session) -> None:
    session.install(".[cli]", "mypy", "nox")
    session.run("mypy", ".")


# TODO
# @nox.session(python=["3.9", "3.10"])
# def test(session: nox.Session) -> None:
#     session.install(".", "pytest")
#     session.run("pytest")
