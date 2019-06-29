from collections import namedtuple
from typing import List

from src.hacker_rank.data_structures.arrays.left_rotate import rot_left

Case = namedtuple("TestCase", "n expected")


# https://www.hackerrank.com/challenges/array-left-rotation/problem
def test_frequency():
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
        n, expected = case  # type: int, List[int]
        assert rot_left(arr, n) == expected
