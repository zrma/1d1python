from src.hacker_rank.python.basic_data_types import *


# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
class TestBasicDataTypes:
    def test_find_the_runner_up_score(self):
        assert find_the_runner_up_score([2, 3, 6, 6, 5]) == 5
        assert find_the_runner_up_score([57, 57, -57, 57]) == -57
