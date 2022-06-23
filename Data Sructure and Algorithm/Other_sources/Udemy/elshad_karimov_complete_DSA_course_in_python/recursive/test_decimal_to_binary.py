import pytest
from decimal_to_binary import decimal_to_binary


def test_decimal_to_binary():
    assert decimal_to_binary(11) == 1011
    assert decimal_to_binary(-11) == 1011
    assert decimal_to_binary(32) == 100000
    assert decimal_to_binary(0) == 0
    with pytest.raises(Exception):
        assert decimal_to_binary(11.1)
        assert decimal_to_binary(-123.123)

