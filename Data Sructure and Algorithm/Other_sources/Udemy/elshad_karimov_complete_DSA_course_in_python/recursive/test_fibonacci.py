import pytest
from fibonacci import fibonacci


def test_fibonacci():
    assert fibonacci(11) == 89
    assert fibonacci(0) == 0
    with pytest.raises(Exception):
        assert fibonacci(-1)
        assert fibonacci(1.5)
