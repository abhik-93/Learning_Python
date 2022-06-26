from checkIsOdd import checkOdd, isOdd


def test_checkOdd():
    assert checkOdd([1, 2, 3, 4], isOdd) is True
    assert checkOdd([2, 4, 6, 8], isOdd) is False
    assert checkOdd([], isOdd) is False
    assert checkOdd([0, 0, -2, -1.4], isOdd) is False
