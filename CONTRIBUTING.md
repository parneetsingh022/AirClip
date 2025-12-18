# Contributing to AirClip

Thank you for your interest in contributing to AirClip, a secure P2P clipboard synchronization tool. We welcome contributions from everyone.

## Getting Started
### Prerequisites
* Python 3.11 or higher is required.
* It is recommended to use a virtual environment (e.g., venv or conda).

### Setup Instructions
1. Clone the repository:
```bash
git clone https://github.com/parneetsingh022/AirClip.git
cd AirClip
```

2. Install development dependencies: The project uses `pyproject.toml` to manage dependencies. Install the package in editable mode with development tools:
```bash
pip install -e .[dev]
```

3. Set up pre-commit hooks: We use `pre-commit` to ensure code quality before every commit.
```bash
pre-commit install
```

## Development Workflow
### Coding Standards
We use the following tools to maintain code quality:
* **Linting & Formatting**: We use Ruff for linting and formatting.
* **Type Checking**: We use MyPy for static type analysis.
* **Security**: We use Bandit to check for common security issues.

## Running Tests
All tests are located in the `tests/` directory and use pytest.
```bash
pytest
```

## Pull Request Process
1. **Create a Branch**: Create a descriptive branch name for your feature or bug fix.

2. **Implement and Test**: Develop your changes and include corresponding tests to verify the new logic or fix.

3. **Commit Changes**: Ensure your changes pass the local pre-commit hooks (trailing whitespace, Ruff, and MyPy).

4. **Submit PR**: Open a Pull Request against the main branch.

5. **Review**: Once the CI pipeline passes, a maintainer will review your changes.

## License
By contributing to AirClip, you agree that your contributions will be licensed under the Apache License 2.0.
