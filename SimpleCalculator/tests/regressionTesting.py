
from calculator.add import add
from calculator.sub import sub
from calculator.multiplication import multiply  # noqa: F401
from calculator.division import divide
from calculator.negate import negate


def test_regression_add_zero():
    assert add(0, 0) == 0


def test_regression_divide_by_one():
    assert divide(5, 1) == 5


def test_regression_negate_twice():
    value = negate(negate(5))
    assert value == 5


def test_regression_chain():
    result = negate(add(2, sub(5, 3)))  # negate(2 + (5-3)) = negate(4) = -4
    assert result == -4
