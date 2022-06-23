def recursive_range_sum(num):
    assert int(num) == num and num > 0, 'Number must be Positive Integer'
    if num == 1:
        return 1
    else:
        return num + recursive_range_sum(num-1)
