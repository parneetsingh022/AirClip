from pygha import default_pipeline, job
from pygha.steps import uses, checkout, echo, shell

default_pipeline(
    on_pull_request=['main'],
    on_push=['main']
)

@job(
    name="tests",
    matrix={"python": ["3.11", "3.12", "3.13", "3.14"]},
)
def tests():
    echo("Testing python version ${{matrix.python}}")
    checkout()
    uses(
        "actions/setup-python@v5",
        with_args={"python-version": "${{ matrix.python }}"},
    )

    shell("pip install .[dev]")
    shell("pytest")