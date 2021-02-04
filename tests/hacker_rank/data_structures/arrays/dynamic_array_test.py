from dataclasses import dataclass
from typing import Sequence, Tuple

from src.hacker_rank.data_structures.arrays.dynamic_array import dynamic_array


# https://www.hackerrank.com/challenges/2d-array/problem
def test_frequency():
    @dataclass
    class Case:
        n: int
        queries: Sequence[Tuple[int, int, int]]
        expected: Sequence[int]

    cases = (
        Case(n=2,
             queries=(
                 (1, 0, 5),
                 (1, 1, 7),
                 (1, 0, 3),
                 (2, 1, 0),
                 (2, 1, 1),
             ),
             expected=[7, 3],
             ),
    )

    for case in cases:
        assert dynamic_array(case.n, case.queries) == case.expected
