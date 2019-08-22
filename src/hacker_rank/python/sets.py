from typing import Sequence


def average(arr: Sequence[int]) -> float:
    s = set(arr)
    return sum(s) / len(s)
