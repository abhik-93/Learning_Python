import pytest
from factorial import factorial


def test_factorial():
    assert factorial(10) == 3628800
    assert factorial(0) == 1
    with pytest.raises(Exception):
        assert factorial(-1)
        assert factorial(1.5)
