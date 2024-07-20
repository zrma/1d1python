from typing import Sequence

import attrs

from src.hacker_rank.data_structures.arrays.dynamic_array import dynamic_array


def test_frequency() -> None:
    """
    https://www.hackerrank.com/challenges/2d-array/problem
    2D Array - DS
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        n: int
        queries: Sequence[tuple[int, int, int]]
        want: Sequence[int]

    for tt in (
        TestCase(
            n=2,
            queries=(
                (1, 0, 5),
                (1, 1, 7),
                (1, 0, 3),
                (2, 1, 0),
                (2, 1, 1),
            ),
            want=[7, 3],
        ),
    ):
        got = dynamic_array(tt.n, tt.queries)
        assert got == tt.want
