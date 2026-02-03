# MathExample

This repository provides basic math operations (addition and subtraction) implemented in Python, along with corresponding pytest-based test cases and CI workflow integration.

## Usage

Import the functions from `src/math_operations.py`:

```python
from src.math_operations import add, subtract

print(add(2, 3))        # Output: 5
print(subtract(5, 2))   # Output: 3
```

## Testing

Run all tests using pytest:

```sh
python -m pytest tests/ -v --tb=short
```

## Workflow

This repository supports GitHub Actions CI via `.github/workflows/ci.yml`.

## Requirements

- Python >= 3.10
- pytest

See `default/requirements.txt` for dependencies.
