import pytest
from src.math_operations import subtract

def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2

def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2

def test_subtract_zero():
    assert subtract(0, 0) == 0

def test_subtract_positive_and_negative():
    assert subtract(5, -3) == 8

def test_subtract_large_numbers():
    assert subtract(2_000_000, 1_000_000) == 1_000_000

def test_subtract_float_numbers():
    assert subtract(5.5, 2.1) == pytest.approx(3.4)

def test_subtract_int_and_float():
    assert subtract(5, 2.5) == pytest.approx(2.5)
