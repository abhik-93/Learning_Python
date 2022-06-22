import pytest
from power_of_num import power_of_num


def test_power_of_num():
    assert power_of_num(12, 2) == 144
    assert power_of_num(0, 0) == 1
    with pytest.raises(Exception):
        assert power_of_num(-12, 2)
        assert power_of_num(12, -2)
        assert power_of_num(0.1, 2)
        assert power_of_num(4, 2.1)
