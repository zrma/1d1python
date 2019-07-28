from random import randint
from collections import namedtuple

from src.hacker_rank.python.introduction import *


# https://www.hackerrank.com/challenges/python-arithmetic-operators/problem
# noinspection SpellCheckingInspection
def test_arithmetic_operators(capsys):  # noqa
    for _ in range(100):
        a = randint(1, 1000000)
        b = randint(1, 1000000)

        arithmetic_operators(a, b)
        captured = capsys.readouterr()
        assert captured.out == f"{a + b}\n{a - b}\n{a * b}\n"


# https://www.hackerrank.com/challenges/python-division/problem
# noinspection SpellCheckingInspection
def test_division(capsys):  # noqa
    for _ in range(100):
        a = randint(1, 1000000)
        b = randint(1, 1000000)

        division(a, b)
        captured = capsys.readouterr()
        assert captured.out == f"{a // b}\n{a / b}\n"


# https://www.hackerrank.com/challenges/py-hello-world/problem
# noinspection SpellCheckingInspection
def test_hello_world(capsys):  # noqa
    hello_world()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"


Case = namedtuple("TestCase", "n expected desc")


# https://www.hackerrank.com/challenges/py-if-else/problem
# noinspection SpellCheckingInspection
def test_if_else(capsys):  # noqa
    cases = (
        Case(n=1, expected="Weird", desc="홀수"),
        Case(n=3, expected="Weird", desc="홀수"),
        Case(n=5, expected="Weird", desc="홀수"),
        Case(n=21, expected="Weird", desc="홀수"),
        Case(n=2, expected="Not Weird", desc="2~5"),
        Case(n=4, expected="Not Weird", desc="2~5"),
        Case(n=6, expected="Weird", desc="6~20"),
        Case(n=20, expected="Weird", desc="6~20"),
        Case(n=22, expected="Not Weird", desc="greater than 20"),
    )

    for case in cases:
        if_else(case.n)
        captured = capsys.readouterr()
        assert captured.out == f"{case.expected}\n", case.desc


# https://www.hackerrank.com/challenges/python-loops/problem
# noinspection SpellCheckingInspection
def test_loops(capsys):  # noqa
    loops(5)
    captured = capsys.readouterr()
    assert captured.out == f"0\n1\n4\n9\n16\n"


# https://www.hackerrank.com/challenges/python-print/problem
# noinspection SpellCheckingInspection
def test_print_function(capsys):  # noqa
    print_function(3)
    captured = capsys.readouterr()
    assert captured.out == "123\n"


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
