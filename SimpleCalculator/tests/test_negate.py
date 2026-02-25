import pytest
from calculator.negate import negate

def test_negate_positive():
    assert negate(5) == -5

def test_negate_negative():
    assert negate(-5) == 5

def test_negate_zero():
    assert negate(0) == 0

def test_negate_float():
    assert pytest.approx(negate(2.5), 0.01) == -2.5
    assert pytest.approx(negate(-2.5), 0.01) == 2.5
