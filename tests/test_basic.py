import pathlib
import airclip
import tomllib  # Available in Python 3.11+


def test_versions_are_aligned():
    """
    Checks if the version in pyproject.toml matches the version 
    defined in src/airclip/__init__.py
    """
    # 1. Get the path to pyproject.toml
    # Assumes the test is running from the root or 'tests/' directory
    root_path = pathlib.Path(__file__).parent.parent
    pyproject_path = root_path / "pyproject.toml"
    
    # 2. Parse the pyproject.toml file
    with open(pyproject_path, "rb") as f:
        pyproject_data = tomllib.load(f)
    
    pyproject_version = pyproject_data.get("project", {}).get("version")
    
    # 3. Get the version from the package
    package_version = airclip.__version__
    
    # 4. Assert they are the same
    assert pyproject_version == package_version, (
        f"Version mismatch! pyproject.toml: {pyproject_version} != "
        f"__init__.py: {package_version}"
    )
