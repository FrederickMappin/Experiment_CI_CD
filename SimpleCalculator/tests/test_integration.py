
from calculator.add import add
from calculator.sub import sub
from calculator.multiplication import multiply
from calculator.division import divide
from calculator.negate import negate


def test_add_and_negate():
    result = add(2, 3)
    neg = negate(result)
    assert result == 5
    assert neg == -5


def test_sub_and_negate():
    result = sub(5, 2)
    neg = negate(result)
    assert result == 3
    assert neg == -3


def test_multiply_and_negate():
    result = multiply(4, 2)
    neg = negate(result)
    assert result == 8
    assert neg == -8


def test_divide_and_negate():
    result = divide(10, 2)
    neg = negate(result)
    assert result == 5
    assert neg == -5


def test_chain_operations():
    result = add(2, multiply(3, 4))  # 2 + (3*4) = 14
    neg = negate(result)

    assert result == 14
    assert neg == -14
