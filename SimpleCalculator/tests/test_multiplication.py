import pytest
from calculator.multiplication import multiply

def test_multiply_positive():
    assert multiply(2, 3) == 6

def test_multiply_negative():
    assert multiply(-2, -3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(2, -3) == -6

def test_multiply_zero():
    assert multiply(0, 5) == 0
    assert multiply(5, 0) == 0
    assert multiply(0, 0) == 0

def test_multiply_float():
    assert pytest.approx(multiply(2.5, 4), 0.01) == 10.0
