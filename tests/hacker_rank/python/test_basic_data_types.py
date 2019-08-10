from src.hacker_rank.python.basic_data_types import *


class TestBasicDataTypes:
    # https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
    def test_find_the_runner_up_score(self):
        assert find_the_runner_up_score([2, 3, 6, 6, 5]) == 5
        assert find_the_runner_up_score([57, 57, -57, 57]) == -57

    # https://www.hackerrank.com/challenges/list-comprehensions/problem
    def test_list_comprehensions(self):
        assert list_comprehensions(1, 1, 1, 2) == \
               [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
        assert list_comprehensions(2, 2, 2, 2) == \
               [[0, 0, 0], [0, 0, 1], [0, 1, 0],
                [0, 1, 2], [0, 2, 1], [0, 2, 2],
                [1, 0, 0], [1, 0, 2], [1, 1, 1],
                [1, 1, 2], [1, 2, 0], [1, 2, 1],
                [1, 2, 2], [2, 0, 1], [2, 0, 2],
                [2, 1, 0], [2, 1, 1], [2, 1, 2],
                [2, 2, 0], [2, 2, 1], [2, 2, 2]]
