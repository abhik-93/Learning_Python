def isOdd(num: int) -> bool:
    if int(num) != num:
        return False
    if num % 2 == 0:
        return False
    else:
        return True


def checkOdd(arr: list, func: callable) -> bool:
    if len(arr) > 0:
        if func(arr[-1]):
            return True
        else:
            return checkOdd(arr[:-1], isOdd)
    else:
        return False
