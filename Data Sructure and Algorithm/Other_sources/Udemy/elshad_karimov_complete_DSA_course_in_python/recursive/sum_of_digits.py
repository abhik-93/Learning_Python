# Using iteration
def sum_of_digits_iteration(n: int) -> int:
    assert int(n) == n and n >= 0, 'Sum of digit is only for Positive Integers'
    sum_ = 0
    while n > 0:
        sum_ += n % 10
        n //= 10
    return sum_


# Using recursion
def sum_of_digits_recursion(n: int) -> int:
    assert int(n) == n and n >= 0, 'Sum of digit is only for Positive Integers'
    if n == 0:
        return 0
    return n % 10 + sum_of_digits_recursion(n // 10)
