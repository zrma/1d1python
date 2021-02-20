from src.hacker_rank.python.sets import average
from src.hacker_rank.python.sets import no_idea
from src.hacker_rank.python.sets import symmetric_difference


# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
def test_average():
    assert average([
        161, 182, 161, 154, 176, 170, 167, 171, 170, 174
    ]) == 169.375


# https://www.hackerrank.com/challenges/symmetric-difference/problem
def test_symmetric_difference():
    assert symmetric_difference({2, 4, 5, 9}, {2, 4, 11, 12}) == [5, 9, 11, 12]
    assert symmetric_difference({8, -10}, {5, 6, 7}) == [-10, 5, 6, 7, 8]


# https://www.hackerrank.com/challenges/no-idea/problem
def test_no_idea():
    assert no_idea([1, 5, 3], {3, 1}, {5, 7}) == 1
