def power_of_num(base: int, exp: int) -> int:
    assert int(base) == base and int(exp) == exp and base >= 0 and exp >= 0, 'Base and Exp needs to be positive'
    if exp > 0:
        return base * power_of_num(base, exp - 1)
    else:
        return 1
