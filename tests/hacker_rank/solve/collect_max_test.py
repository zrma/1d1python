from collections import namedtuple

from src.hacker_rank.solve.collect_max import collect_max, mul_mat

Case = namedtuple("TestCase", "data expected")


def test_collect_max():
    cases = (
        Case(data=(
            (0, 1, -1),
            (1, 0, -1),
            (1, 1, 1),
        ),
            expected=5),
        Case(data=(
            (0, 1, 1),
            (1, 0, 1),
            (1, 1, 1)
        ),
            expected=7),
        Case(data=(
            (0, 1, 1),
            (1, 0, -1),
            (1, 1, -1)
        ),
            expected=0),
    )

    for case in cases:
        actual = collect_max(case.data)
        assert case.expected == actual


def test_mul_mat():
    cases = (
        Case(data=(
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
        Case(data=(
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
        Case(data=(
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
        actual = mul_mat(*case.data)
        assert case.expected == actual
