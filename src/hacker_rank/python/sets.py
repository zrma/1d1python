from typing import Sequence


def average(arr: Sequence[int]) -> float:
    s = set(arr)
    return sum(s) / len(s)


def symmetric_difference(s1: set, s2: set) -> list:
    return sorted(s1 ^ s2)


def no_idea(arr: Sequence[int], s1: set, s2: set) -> int:
    s1_1 = s1 - s2
    s2_1 = s2 - s1

    happiness = 0
    for i in arr:
        if i in s1_1:
            happiness += 1

    for i in arr:
        if i in s2_1:
            happiness -= 1

    return happiness
