def fibonacci(n: int) -> int:
    """This function returns nth fibonacci number"""
    assert int(n) == n and n >= 0, "Fibonacci series always has a positive integer as input!"
    if n in (0, 1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
