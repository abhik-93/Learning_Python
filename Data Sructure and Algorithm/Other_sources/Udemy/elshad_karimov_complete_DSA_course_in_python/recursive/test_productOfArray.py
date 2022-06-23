import pytest
from productOfArray import product_of_array


def test_product_of_array():
    assert product_of_array([1, 2, 3, 4, 5]) == 120
    assert product_of_array([-1, 2, 3, 4, 5]) == -120
    assert product_of_array([1, 2, 3, 10]) == 60
    with pytest.raises(Exception):
        assert product_of_array(1235)
