import nox


@nox.session
def format(session: nox.Session) -> None:
    session.install("black", "isort")
    session.run("isort", ".")
    session.run("black", ".")


@nox.session
def check_format(session: nox.Session):
    session.install("black", "isort")
    session.run("isort", ".", "--check")
    session.run("black", ".", "--check")


@nox.session
def lint(session: nox.Session) -> None:
    session.install(
        "pyproject-flake8",
        "flake8-annotations",
        "flake8-bugbear",
        "flake8-docstrings",
    )
    session.run("pflake8", "makemkv/", "noxfile.py")


@nox.session
def mypy(session: nox.Session) -> None:
    session.install(".[cli,test]", "mypy")
    session.run("mypy")


@nox.session(python=["3.9", "3.10", "3.11"])
def test(session: nox.Session) -> None:
    session.install("-e", ".[test]")
    session.run(
        "pytest",
        "--cov",
        "--cov-report=xml",
        "--cov-report=term",
    )
