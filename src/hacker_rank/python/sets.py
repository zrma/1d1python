from typing import Sequence


def average(arr: Sequence[int]) -> float:
    s = set(arr)
    return sum(s) / len(s)


def symmetric_difference(s1: set, s2: set) -> list:
    return sorted(s1 ^ s2)
