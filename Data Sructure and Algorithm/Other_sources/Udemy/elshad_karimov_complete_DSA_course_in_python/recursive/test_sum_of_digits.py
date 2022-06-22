import pytest
from sum_of_digits import *


def test_sum_of_digits_iteration():
    assert sum_of_digits_iteration(123456789) == 45
    assert sum_of_digits_iteration(0) == 0
    with pytest.raises(Exception):
        assert sum_of_digits_iteration(-1234) == 0


def test_sum_of_digits_recursion():
    assert sum_of_digits_recursion(123456789) == 45
    assert sum_of_digits_recursion(0) == 0
    with pytest.raises(Exception):
        assert sum_of_digits_recursion(-123456789)
        assert sum_of_digits_recursion(-1234567.89)
        assert sum_of_digits_recursion(1234567.89)
        assert sum_of_digits_recursion('asda')
