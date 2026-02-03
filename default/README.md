# MathExample

This repository provides basic math operations (addition and subtraction) in Python, along with corresponding tests and CI workflow integration.

## Usage

Import the functions from `src/math_operations.py`:

```python
from src.math_operations import add, subtract

result = add(2, 3)
print(result)  # 5

result = subtract(5, 2)
print(result)  # 3
```

## Testing

Run tests using pytest:

```bash
python -m pytest tests/ -v --tb=short
```

## CI/CD

The repository is configured for CI using GitHub Actions. Workflow file: `.github/workflows/ci.yml`.
