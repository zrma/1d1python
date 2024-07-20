from typing import Iterable

import attrs

from src.hacker_rank.interview_preparation_kit.array.array_manipulation import array_manipulation


def test_array_manipulation() -> None:
    """
    https://www.hackerrank.com/challenges/crush/problem
    Array Manipulation
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        n: int
        queries: Iterable[tuple[int, int, int]]
        want: int

    for tt in (
        TestCase(
            n=10,
            queries=(
                (1, 5, 3),
                (4, 8, 7),
                (6, 9, 1),
            ),
            want=10,
        ),
        TestCase(
            n=5,
            queries=(
                (1, 2, 100),
                (2, 5, 100),
                (3, 4, 100),
            ),
            want=200,
        ),
        TestCase(
            n=10,
            queries=(
                (2, 6, 8),
                (3, 5, 7),
                (1, 8, 1),
                (5, 9, 15),
            ),
            want=31,
        ),
        TestCase(
            n=10,
            queries=(
                (3, 5, 7),
                (2, 6, 8),
                (1, 8, 1),
                (5, 9, 15),
            ),
            want=31,
        ),
    ):
        got = array_manipulation(tt.n, tt.queries)
        assert got == tt.want
