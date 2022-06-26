def reverse(string: str) -> str:
    if len(string) == 1:
        return string[0]
    return string[-1] + reverse(string[:-1])
