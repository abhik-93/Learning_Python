def product_of_array(arr: list) -> int:
    assert isinstance(arr, list), 'Input is expected as list'
    if len(arr) > 0:
        return arr[-1] * product_of_array(arr[:-1])
    else:
        return 1
