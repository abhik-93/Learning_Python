def factorial(n: int) -> int:
    """This function returns nth factorial value"""
    assert int(n) == n and n >= 0, "Factorial can be always of a positive integer!"
    if n in (0,1):
        return 1
    else:
        return n * factorial(n-1)
