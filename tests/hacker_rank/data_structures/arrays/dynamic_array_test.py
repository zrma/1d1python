from collections import namedtuple
from typing import Sequence

from src.hacker_rank.data_structures.arrays.dynamic_array import dynamic_array

Case = namedtuple("TestCase", "n queries expected")


def test_frequency():
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
        n, queries, expected = case  # type: int, Sequence[Sequence[int]], int
        assert expected == dynamic_array(n, queries)
