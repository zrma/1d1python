import unittest
from collections import namedtuple
from typing import List

from src.hacker_rank.solve.collect_max import collect_max, mul_mat

TestCase = namedtuple("TestCase", "input expected")


class TestDeleteOdd(unittest.TestCase):
    def setUp(self):
        pass

    def test_collect_max(self):
        cases: List[TestCase] = [
            TestCase(input=[
                [0, 1, -1],
                [1, 0, -1],
                [1, 1, 1],
            ],
                expected=5),
            TestCase(input=[
                [0, 1, 1],
                [1, 0, 1],
                [1, 1, 1]
            ],
                expected=7),
            TestCase(input=[
                [0, 1, 1],
                [1, 0, -1],
                [1, 1, -1]
            ],
                expected=0),
        ]

        for case in cases:
            actual = collect_max(case.input)
            self.assertEqual(case.expected, actual)

    def test_mul_mat(self):
        cases: List[TestCase] = [
            TestCase(input=[
                [
                    [1, 0, 1],
                    [1, 1, 1],
                ], [
                    [1, 2],
                    [1, 2],
                    [1, 2],
                ]
            ],
                expected=8),
            TestCase(input=[
                [
                    [1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1],
                ], [
                    [1, 2, 3],
                    [1, 2, 3],
                    [1, 2, 3],
                ]
            ],
                expected=6),
            TestCase(input=[
                [
                    [1, 1],
                    [0, 1],
                    [0, 0],
                ], [
                    [1, 2, 3],
                    [1, 2, 3],
                ]
            ],
                expected=4),
        ]

        for case in cases:
            actual = mul_mat(*case.input)
            self.assertEqual(case.expected, actual)
