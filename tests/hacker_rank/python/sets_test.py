from src.hacker_rank.python.sets import *


class TestSets:
    # https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
    def test_average(self):
        assert average([
            161, 182, 161, 154, 176, 170, 167, 171, 170, 174
        ]) == 169.375
