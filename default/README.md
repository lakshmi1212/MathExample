# MathExample

A simple Python project implementing basic math operations (addition and subtraction) with automated tests and CI workflow integration.

## Project Structure

- `src/math_operations.py` - Core math functions (add, subtract)
- `tests/test_add.py` - Pytest cases for addition
- `tests/test_subtract.py` - Pytest cases for subtraction
- `default/requirements.txt` - Python dependencies
- `default/README.md` - This documentation
- `default/math.json` - CI workflow metadata for automation

## Usage

1. **Install dependencies**

```bash
pip install -r default/requirements.txt
```

2. **Run tests**

```bash
pytest tests/ -v --tb=short
```

## CI/CD Integration

The repository is designed for seamless CI integration. Workflow metadata is provided in `default/math.json` for use by automation agents to generate workflow YAML files.

## Python Version

Python >= 3.10 is required.

## License

MIT
