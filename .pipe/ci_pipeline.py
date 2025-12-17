from pygha import default_pipeline, job
from pygha.steps import uses, checkout, echo, shell

PYTHON_VERSIONS = ["3.11", "3.12", "3.13", "3.14"]
SUPPORTED_OS =  ["ubuntu-latest", "macos-latest", "windows-latest"]

def setup_python(version="3.12"):
    uses(
        "actions/setup-python@v5", 
        with_args={
            "python-version": version,
            "cache": "pip"
        }
    )

default_pipeline(
    on_pull_request=['main'],
    on_push=['main']
)


@job(name="lint")
def lint():
    checkout()
    uses("actions/setup-python@v5", with_args={"python-version": "3.12"})
    shell("pip install ruff")
    shell("ruff check .") # Fast failure if code is messy

@job(
    name="tests",
    runs_on="${{matrix.os}}",
    matrix={"python": PYTHON_VERSIONS, "os": SUPPORTED_OS},
    depends_on=['lint']
)
def tests():
    echo("Testing ${{matrix.python}} on ${{matrix.os}}")

    checkout()
    setup_python("${{matrix.python}}")

    shell("pip install .[dev]")
    shell("pytest")