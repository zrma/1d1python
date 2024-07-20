from typing import Sequence

import attrs

from src.hacker_rank.interview_preparation_kit.array.ds_2d_array import hourglass_sum


def test_hourglass_sum() -> None:
    """
    https://www.hackerrank.com/challenges/2d-array/problem
    2D Array - DS
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        name: str
        give: Sequence[Sequence[int]]
        want: int

    for i, tt in enumerate(
        (
            TestCase(
                name="Normal",
                give=(
                    (-9, -9, -9, 1, 1, 1),
                    (0, -9, 0, 4, 3, 2),
                    (-9, -9, -9, 1, 2, 3),
                    (0, 0, 8, 6, 6, 0),
                    (0, 0, 0, -2, 0, 0),
                    (0, 0, 1, 2, 4, 0),
                ),
                want=28,
            ),
            TestCase(
                name="Normal",
                give=(
                    (1, 1, 1, 0, 0, 0),
                    (0, 1, 0, 0, 0, 0),
                    (1, 1, 1, 0, 0, 0),
                    (0, 0, 2, 4, 4, 0),
                    (0, 0, 0, 2, 0, 0),
                    (0, 0, 1, 2, 4, 0),
                ),
                want=19,
            ),
            TestCase(
                name="Abnormal",
                give=(
                    (1, 2),
                    (3, 4),
                    (5, 6),
                    (7, 8),
                ),
                want=0,
            ),
            TestCase(
                name="Abnormal",
                give=(
                    (1, 2),
                    (3, 4),
                ),
                want=0,
            ),
        )
    ):
        got = hourglass_sum(tt.give)
        assert got == tt.want, f"{i}/{tt.name}"
