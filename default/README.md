# MathExample

This repository contains basic math operations (addition and subtraction) implemented in Python, with comprehensive pytest test coverage and CI/CD workflow integration.

## Structure
- `src/math_operations.py`: Core math logic
- `tests/test_add.py`: Tests for addition
- `tests/test_subtract.py`: Tests for subtraction
- `default/requirements.txt`: Project dependencies
- `default/math.json`: CI workflow metadata

## Usage

1. **Install dependencies:**
   ```bash
   pip install -r default/requirements.txt
   ```
2. **Run tests:**
   ```bash
   python -m pytest tests/ -v --tb=short
   ```

## CI/CD
- See `.github/workflows/ci.yml` for the workflow (referenced via `math.json`).

## Python Version
- Requires Python 3.10 or compatible.
