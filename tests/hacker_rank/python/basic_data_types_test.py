from src.hacker_rank.python.basic_data_types import find_the_runner_up_score
from src.hacker_rank.python.basic_data_types import finding_the_percentage
from src.hacker_rank.python.basic_data_types import list_comprehensions
from src.hacker_rank.python.basic_data_types import lists
from src.hacker_rank.python.basic_data_types import nested_lists
from src.hacker_rank.python.basic_data_types import tuples


# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
def test_find_the_runner_up_score():
    assert find_the_runner_up_score([2, 3, 6, 6, 5]) == 5
    assert find_the_runner_up_score([57, 57, -57, 57]) == -57


# https://www.hackerrank.com/challenges/list-comprehensions/problem
def test_list_comprehensions():
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
def test_nested_lists():
    # noinspection SpellCheckingInspection
    assert nested_lists([
        "Harry", 37.21, "Berry", 37.21, "Tina", 37.2, "Akriti", 41, "Harsh", 39,
    ]) == ["Berry", "Harry"]
    # noinspection SpellCheckingInspection
    assert nested_lists([
        "Rachel", - 50, "Mawer", - 50, "Sheen", - 50, "Shaheen", 51,
    ]) == ["Shaheen"]
    assert nested_lists([]) == []


# https://www.hackerrank.com/challenges/finding-the-percentage/problem
def test_finding_the_percentage():
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


# https://www.hackerrank.com/challenges/python-lists/problem
def test_lists():
    assert lists([
        ["insert", "0", "5"],
        ["insert", "1", "10"],
        ["insert", "0", "6"],
        ["print"],
        ["remove", "6"],
        ["append", "9"],
        ["append", "1"],
        ["sort"],
        ["print"],
        ["pop"],
        ["reverse"],
        ["print"],
    ]) == [[6, 5, 10],
           [1, 5, 9, 10],
           [9, 5, 1]]

    assert lists([
        ["append", "1"],
        ["append", "6"],
        ["append", "10"],
        ["append", "8"],
        ["append", "9"],
        ["append", "2"],
        ["append", "12"],
        ["append", "7"],
        ["append", "3"],
        ["append", "5"],
        ["insert", "8", "66"],
        ["insert", "1", "30"],
        ["insert", "6", "75"],
        ["insert", "4", "44"],
        ["insert", "9", "67"],
        ["insert", "2", "44"],
        ["insert", "9", "21"],
        ["insert", "8", "87"],
        ["insert", "1", "75"],
        ["insert", "1", "48"],
        ["print"],
        ["reverse"],
        ["print"],
        ["sort"],
        ["print"],
        ["append", "2"],
        ["append", "5"],
        ["remove", "2"],
        ["print"],
    ]) == [[1, 48, 75, 30, 44, 6, 10, 44, 8, 9, 87, 75, 21, 2, 67, 12, 7, 66, 3, 5],
           [5, 3, 66, 7, 12, 67, 2, 21, 75, 87, 9, 8, 44, 10, 6, 44, 30, 75, 48, 1],
           [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 21, 30, 44, 44, 48, 66, 67, 75, 75, 87],
           [1, 3, 5, 6, 7, 8, 9, 10, 12, 21, 30, 44, 44, 48, 66, 67, 75, 75, 87, 2, 5]]


# https://www.hackerrank.com/challenges/python-tuples/problem
def test_tuples():
    assert tuples([1, 2]) == -3550055125485641917
