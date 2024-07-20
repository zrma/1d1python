import pytest

from src.hacker_rank.python.sets import average, no_idea, symmetric_difference


def test_average() -> None:
    """
    https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
    Introduction to Sets
    """
    assert average([161, 182, 161, 154, 176, 170, 167, 171, 170, 174]) == pytest.approx(169.375, rel=1e-9)


def test_symmetric_difference() -> None:
    """
    https://www.hackerrank.com/challenges/symmetric-difference/problem
    Symmetric Difference
    """
    assert symmetric_difference({2, 4, 5, 9}, {2, 4, 11, 12}) == [5, 9, 11, 12]
    assert symmetric_difference({8, -10}, {5, 6, 7}) == [-10, 5, 6, 7, 8]


def test_no_idea() -> None:
    """
    https://www.hackerrank.com/challenges/no-idea/problem
    No Idea!
    """
    assert no_idea([1, 5, 3], {3, 1}, {5, 7}) == 1
