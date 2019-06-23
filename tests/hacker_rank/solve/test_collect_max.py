from collections import namedtuple

from src.hacker_rank.solve.collect_max import collect_max, mul_mat

Case = namedtuple("TestCase", "input expected")


def test_collect_max():
    cases = (
        Case(input=(
            (0, 1, -1),
            (1, 0, -1),
            (1, 1, 1),
        ),
            expected=5),
        Case(input=(
            (0, 1, 1),
            (1, 0, 1),
            (1, 1, 1)
        ),
            expected=7),
        Case(input=(
            (0, 1, 1),
            (1, 0, -1),
            (1, 1, -1)
        ),
            expected=0),
    )

    for case in cases:
        actual = collect_max(case.input)
        assert case.expected == actual


def test_mul_mat():
    cases = (
        Case(input=(
            (
                (1, 0, 1),
                (1, 1, 1),
            ), (
                (1, 2),
                (1, 2),
                (1, 2),
            )
        ),
            expected=8),
        Case(input=(
            (
                (1, 0, 0),
                (0, 1, 0),
                (0, 0, 1),
            ), (
                (1, 2, 3),
                (1, 2, 3),
                (1, 2, 3),
            )
        ),
            expected=6),
        Case(input=(
            (
                (1, 1),
                (0, 1),
                (0, 0),
            ), (
                (1, 2, 3),
                (1, 2, 3),
            )
        ),
            expected=4),
    )

    for case in cases:
        actual = mul_mat(*case.input)
        assert case.expected == actual
