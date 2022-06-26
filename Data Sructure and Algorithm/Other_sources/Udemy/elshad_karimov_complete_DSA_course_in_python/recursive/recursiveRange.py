def recursive_range_sum(num: int) -> int:
    assert int(num) == num and num > 0, 'Number must be Positive Integer'
    if num == 1:
        return 1
    return num + recursive_range_sum(num-1)
