from src.hacker_rank.python.introduction.write_a_function import is_leap


# https://www.hackerrank.com/challenges/write-a-function/problem
def test_is_leap():
    for year, expected in [
        (2000, True),
        (2400, True),
        (1800, False),
        (1900, False),
        (2100, False),
        (2200, False),
        (2300, False),
        (2500, False),
        (1, False),
        (4, True),
    ]:
        actual = is_leap(year)
        assert actual == expected
