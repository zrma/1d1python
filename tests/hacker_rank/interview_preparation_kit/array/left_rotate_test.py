from dataclasses import dataclass
from typing import List, Sequence

from src.hacker_rank.interview_preparation_kit.array.left_rotate import rot_left


# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem
def test_frequency():
    @dataclass
    class Case:
        n: int
        expected: Sequence[int]

    arr = [1, 2, 3, 4, 5]
    cases = (
        Case(n=0, expected=[1, 2, 3, 4, 5]),
        Case(n=1, expected=[2, 3, 4, 5, 1]),
        Case(n=2, expected=[3, 4, 5, 1, 2]),
        Case(n=3, expected=[4, 5, 1, 2, 3]),
        Case(n=4, expected=[5, 1, 2, 3, 4]),
        Case(n=5, expected=[1, 2, 3, 4, 5]),
        Case(n=6, expected=[2, 3, 4, 5, 1]),
    )

    for case in cases:
        assert rot_left(arr, case.n) == case.expected
