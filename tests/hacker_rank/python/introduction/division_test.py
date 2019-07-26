from random import randint

from src.hacker_rank.python.introduction.division import division


# https://www.hackerrank.com/challenges/python-division/problem
# noinspection SpellCheckingInspection
def test_division(capsys):  # noqa
    for _ in range(100):
        a = randint(1, 1000000)
        b = randint(1, 1000000)

        division(a, b)
        captured = capsys.readouterr()
        assert captured.out == f"{a // b}\n{a / b}\n"
