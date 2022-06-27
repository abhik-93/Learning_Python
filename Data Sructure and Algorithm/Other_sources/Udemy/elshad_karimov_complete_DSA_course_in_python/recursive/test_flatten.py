from flatten import flatten


def test_flatten():
    assert flatten([1, 2, 3, [4, 5]]) == [1, 2, 3, 4, 5]
    assert flatten([1, [2, [3, 4], [[5]]]]) == [1, 2, 3, 4, 5]
    assert flatten([[1], [2], [3]]) == [1, 2, 3]
    assert flatten([[[[1]]], [[[2]]], [[[[[[[3]]]]]]]]) == [1, 2, 3]
