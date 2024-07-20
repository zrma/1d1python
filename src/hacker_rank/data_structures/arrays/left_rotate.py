from typing import Sequence


def rot_left(arr: list[int], n: int) -> Sequence[int]:
    length = len(arr)

    if n < 1 or n % length == 0:
        return arr

    if n > length:
        n = n % length

    return arr[n:] + arr[:n]
