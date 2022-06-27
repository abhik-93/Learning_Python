from typing import Any


def flatten(arr: Any) -> list:
    final_arr = []
    for _ in arr:
        if isinstance(_, int):
            final_arr.append(_)
        elif isinstance(_, list):
            final_arr.extend(flatten(_))

    return final_arr
