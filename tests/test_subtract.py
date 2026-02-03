import pytest
from src.math_operations import subtract

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (0, 0, 0),
    (-1, -1, 0),
    (1, -1, 2),
    (2.5, 1.5, 1.0),
    (1000000, 500000, 500000),
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected

def test_subtract_type_error():
    with pytest.raises(TypeError):
        subtract('a', 2)
