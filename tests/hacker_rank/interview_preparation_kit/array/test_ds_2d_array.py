from collections import namedtuple
from typing import Sequence

from src.hacker_rank.interview_preparation_kit.array.ds_2d_array import hourglass_sum

Case = namedtuple("TestCase", "data expected desc")


# https://www.hackerrank.com/challenges/2d-array/problem
def test_hourglass_sum():
    cases = (
        Case(data=(
            (-9, -9, -9, 1, 1, 1),
            (0, -9, 0, 4, 3, 2),
            (-9, -9, -9, 1, 2, 3),
            (0, 0, 8, 6, 6, 0),
            (0, 0, 0, -2, 0, 0),
            (0, 0, 1, 2, 4, 0),
        ),
            expected=28,
            desc="",
        ),
        Case(data=(
            (1, 1, 1, 0, 0, 0),
            (0, 1, 0, 0, 0, 0),
            (1, 1, 1, 0, 0, 0),
            (0, 0, 2, 4, 4, 0),
            (0, 0, 0, 2, 0, 0),
            (0, 0, 1, 2, 4, 0),
        ),
            expected=19,
            desc="",
        ),
        Case(data=(
            (1, 2), (3, 4), (5, 6), (7, 8),
        ),
            expected=0,
            desc="",
        ),
    )

    for case in cases:
        data, expected, desc = case  # type: Sequence[Sequence[int]], int, str

        actual = hourglass_sum(data)
        assert case.expected == actual, desc
