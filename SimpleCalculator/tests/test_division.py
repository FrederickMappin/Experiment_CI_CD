
from calculator.division import divide


def test_divide_positive():
    assert divide(6, 3) == 2


def test_divide_negative():
    assert divide(-6, -3) == 2
    assert divide(-6, 3) == -2
    assert divide(6, -3) == -2


def test_divide_float():
    import pytest
    assert pytest.approx(divide(7, 2), 0.01) == 3.5


def test_divide_by_one():
    assert divide(5, 1) == 5


def test_divide_by_zero():
    import pytest

    with pytest.raises(ValueError):
        divide(5, 0)
