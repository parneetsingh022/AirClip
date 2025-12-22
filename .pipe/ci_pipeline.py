from pygha import default_pipeline, job
from pygha.steps import uses, checkout, echo, run, setup_python

PYTHON_VERSIONS = ["3.11", "3.12", "3.13", "3.14"]
DEFAULT_PYTHON_VERSION = "3.12"
SUPPORTED_OS =  ["ubuntu-latest", "macos-latest", "windows-latest"]

default_pipeline(
    on_pull_request=['main'],
    on_push=['main']
)


@job(name="lint")
def lint():
    checkout()
    setup_python(DEFAULT_PYTHON_VERSION, cache="pip")
    run("pip install .[dev]")
    run("ruff check .") # Fast failure if code is messy

@job(name="security")
def security():
    checkout()
    setup_python(DEFAULT_PYTHON_VERSION, cache="pip")
    # Bandit needs the [toml] extra to read your pyproject.toml
    run("pip install .[dev]")
    run("bandit -r src/ -c pyproject.toml")


@job(name="types")
def types():
    checkout()
    setup_python(DEFAULT_PYTHON_VERSION, cache="pip")
    run("pip install .[dev]")
    echo("Running MyPy Type Check...")
    run("mypy") # It will automatically use settings from pyproject.toml

@job(
    name="tests",
    runs_on="${{matrix.os}}",
    matrix={"python": PYTHON_VERSIONS, "os": SUPPORTED_OS},
    depends_on=['lint']
)
def tests():
    echo("Testing ${{matrix.python}} on ${{matrix.os}}")

    checkout()
    setup_python("${{matrix.python}}", cache="pip")

    run("pip install .[dev]")
    run("pytest")

    run("pytest --cov=airclip --cov-report=xml")

    uses(
        "codecov/codecov-action@v5",
        with_args={
            "token": "${{ secrets.CODECOV_TOKEN }}",
            "fail_ci_if_error": True,
            "files": "./coverage.xml",

            "flags": "${{matrix.os}},${{matrix.python}}",
            "name": "airclip-tests"
        }
    )
