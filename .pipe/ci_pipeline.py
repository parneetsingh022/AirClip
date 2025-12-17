from pygha import default_pipeline, job
from pygha.steps import uses, checkout, echo, shell

PYTHON_VERSIONS = ["3.11", "3.12", "3.13", "3.14"]

SUPPORTED_OS =  ["ubuntu-latest", "macos-latest", "windows-latest"]

default_pipeline(
    on_pull_request=['main'],
    on_push=['main']
)

@job(
    name="tests",
    runs_on="${{matrix.os}}",
    matrix={"python": PYTHON_VERSIONS, "os": SUPPORTED_OS},
)
def tests():
    echo("Testing ${{matrix.python}} on ${{matrix.os}}")
    checkout()
    uses(
        "actions/setup-python@v5",
        with_args={"python-version": "${{ matrix.python }}"},
    )

    shell("pip install .[dev]")
    shell("pytest")