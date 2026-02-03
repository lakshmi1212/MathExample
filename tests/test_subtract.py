import sys
sys.path.insert(0, './src')
from math_operations import subtract
import pytest

def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2

def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2

def test_subtract_zero():
    assert subtract(0, 0) == 0

def test_subtract_mixed_sign():
    assert subtract(-5, 3) == -8
    assert subtract(5, -3) == 8

def test_subtract_large_numbers():
    assert subtract(10**6, 10**5) == 900000

def test_subtract_float_numbers():
    assert subtract(5.5, 3.1) == pytest.approx(2.4)

def test_subtract_edge_cases():
    assert subtract(0, -0) == 0
    assert subtract(-0, 0) == 0
