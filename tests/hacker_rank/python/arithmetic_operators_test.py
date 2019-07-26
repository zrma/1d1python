from random import randint

from src.hacker_rank.python.arithmetic_operators import arithmetic_operators


# https://www.hackerrank.com/challenges/python-arithmetic-operators/problem
# noinspection SpellCheckingInspection
def test_arithmetic_operators(capsys):  # noqa
    for _ in range(100):
        a = randint(1, 1000000)
        b = randint(1, 1000000)

        arithmetic_operators(a, b)
        captured = capsys.readouterr()
        assert captured.out == f"{a + b}\n{a - b}\n{a * b}\n"
