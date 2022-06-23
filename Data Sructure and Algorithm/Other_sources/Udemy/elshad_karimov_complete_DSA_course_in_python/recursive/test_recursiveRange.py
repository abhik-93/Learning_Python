import pytest
from recursiveRange import recursive_range_sum


def test_recursive_range_sum():
    assert recursive_range_sum(9) == 45
    with pytest.raises(Exception):
        assert recursive_range_sum(-9)
        assert recursive_range_sum(1.4)
