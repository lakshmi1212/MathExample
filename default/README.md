# MathExample

This repository demonstrates basic math operations (addition and subtraction) with production-quality test automation and CI/CD integration.

## Usage

```python
from src.math_operations import add, subtract

result_add = add(2, 3)        # 5
result_subtract = subtract(5, 2)  # 3
```

## Testing

Run all tests using pytest:

```sh
python -m pytest tests/ -v --tb=short
```

## Workflow

- All code is in `src/`
- All tests are in `tests/`
- CI workflow is defined in `.github/workflows/ci.yml`
- Metadata for workflow is in `default/math.json`

## Requirements

- Python 3.10+
- pytest
