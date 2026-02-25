
from calculator.sub import sub


def test_sub_positive():
    assert sub(5, 3) == 2


def test_sub_negative():
    assert sub(-5, -3) == -2
    assert sub(-5, 3) == -8
    assert sub(5, -3) == 8


def test_sub_zero():
    assert sub(0, 0) == 0
    assert sub(0, 5) == -5
    assert sub(5, 0) == 5


def test_sub_float():
    import pytest
    assert pytest.approx(sub(5.5, 2.2), 0.01) == 3.3
