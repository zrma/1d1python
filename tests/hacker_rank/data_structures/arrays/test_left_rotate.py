from typing import Sequence

import attrs

from src.hacker_rank.data_structures.arrays.left_rotate import rot_left


def test_frequency() -> None:
    """
    https://www.hackerrank.com/challenges/array-left-rotation/problem
    Arrays: Left Rotation
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        n: int
        want: Sequence[int]

    for tt in (
        TestCase(n=0, want=[1, 2, 3, 4, 5]),
        TestCase(n=1, want=[2, 3, 4, 5, 1]),
        TestCase(n=2, want=[3, 4, 5, 1, 2]),
        TestCase(n=3, want=[4, 5, 1, 2, 3]),
        TestCase(n=4, want=[5, 1, 2, 3, 4]),
        TestCase(n=5, want=[1, 2, 3, 4, 5]),
        TestCase(n=6, want=[2, 3, 4, 5, 1]),
    ):
        give = [1, 2, 3, 4, 5]
        got = rot_left(give, tt.n)
        assert got == tt.want
