from gcd import gcd
import pytest


def test_gcd():
    assert gcd(48, 18) == 6
    assert gcd(0, 12) == 12
    assert gcd(12, 0) == 12
    assert gcd(-48, 18) == 6
    assert gcd(48, -18) == 6
    with pytest.raises(Exception):
        assert gcd(1.2, 2.4)
        assert gcd(-1.2, 12)
