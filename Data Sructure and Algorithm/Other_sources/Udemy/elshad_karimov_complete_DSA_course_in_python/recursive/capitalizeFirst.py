from typing import Any


def capitalizeFirst(arr: Any) -> Any:
    final_arr = []
    if len(arr) == 0:
        return final_arr
    final_arr.append(arr[0][0].upper() + arr[0][1:])
    return final_arr + capitalizeFirst(arr[1:])
