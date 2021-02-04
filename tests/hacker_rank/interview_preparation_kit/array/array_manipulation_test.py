from dataclasses import dataclass
from typing import Iterable, Tuple

from src.hacker_rank.interview_preparation_kit.array.array_manipulation import array_manipulation


# https://www.hackerrank.com/challenges/crush/problem
def test_array_manipulation():
    @dataclass
    class Case:
        n: int
        queries: Iterable[Tuple[int, int, int]]
        expected: int

    cases = (
        Case(n=10,
             queries=(
                 (1, 5, 3),
                 (4, 8, 7),
                 (6, 9, 1),
             ),
             expected=10),
        Case(n=5,
             queries=(
                 (1, 2, 100),
                 (2, 5, 100),
                 (3, 4, 100),
             ),
             expected=200),
        Case(n=10,
             queries=(
                 (2, 6, 8),
                 (3, 5, 7),
                 (1, 8, 1),
                 (5, 9, 15),
             ),
             expected=31),
        Case(n=10,
             queries=(
                 (3, 5, 7),
                 (2, 6, 8),
                 (1, 8, 1),
                 (5, 9, 15),
             ),
             expected=31),
    )

    for case in cases:
        actual = array_manipulation(case.n, case.queries)
        assert actual == case.expected
