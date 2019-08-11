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

    # https://www.hackerrank.com/challenges/nested-list/problem
    def test_nested_lists(self):
        # noinspection SpellCheckingInspection
        assert nested_lists([
            "Harry", 37.21, "Berry", 37.21, "Tina", 37.2, "Akriti", 41, "Harsh", 39,
        ]) == ["Berry", "Harry"]
        # noinspection SpellCheckingInspection
        assert nested_lists([
            "Rachel", - 50, "Mawer", - 50, "Sheen", - 50, "Shaheen", 51,
        ]) == ["Shaheen"]

    # https://www.hackerrank.com/challenges/finding-the-percentage/problem
    def test_finding_the_percentage(self):
        # noinspection SpellCheckingInspection
        assert finding_the_percentage("Malika", {
            "Krishna": [67, 68, 69],
            "Arjun": [70, 98, 63],
            "Malika": [52, 56, 60],
        }) == "56.00"
        # noinspection SpellCheckingInspection
        assert finding_the_percentage("Malika", {}) == "0.00"
        # noinspection SpellCheckingInspection
        assert finding_the_percentage("Malika", {
            "Malika": [],
        }) == "0.00"
