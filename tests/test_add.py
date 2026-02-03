import sys
sys.path.insert(0, './src')
from math_operations import add
import pytest

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_zero():
    assert add(0, 0) == 0

def test_add_mixed_sign():
    assert add(-2, 3) == 1
    assert add(2, -3) == -1

def test_add_large_numbers():
    assert add(10**6, 10**6) == 2*10**6

def test_add_float_numbers():
    assert add(2.5, 3.1) == pytest.approx(5.6)

def test_add_edge_cases():
    assert add(0, -0) == 0
    assert add(-0, 0) == 0
