from secrets import randbelow

import attrs
import pytest
from pytest import CaptureFixture

from src.hacker_rank.python.introduction import (
    arithmetic_operators,
    division,
    hello_world,
    if_else,
    is_leap,
    loops,
    print_function,
)


@pytest.mark.parametrize("_", range(100))
def test_arithmetic_operators(_: int, capsys: CaptureFixture[str]) -> None:
    """
    https://www.hackerrank.com/challenges/python-arithmetic-operators/problem
    Arithmetic Operators
    """
    a = randbelow(1_000_000) + 1
    b = randbelow(1_000_000) + 1

    arithmetic_operators(a, b)

    want = f"""{a + b}
{a - b}
{a * b}
"""
    got = capsys.readouterr().out
    assert got == want


@pytest.mark.parametrize("_", range(100))
def test_division(_: int, capsys: CaptureFixture[str]) -> None:
    """
    https://www.hackerrank.com/challenges/python-division/problem
    Python: Division
    """
    a = randbelow(1000000) + 1
    b = randbelow(1000000) + 1

    division(a, b)

    want = f"""{a // b}
{a / b}
"""
    got = capsys.readouterr().out
    assert got == want


def test_hello_world(capsys: CaptureFixture[str]) -> None:
    # noinspection GrazieInspection,StructuralWrap
    """
    https://www.hackerrank.com/challenges/py-hello-world/problem
    Say "Hello, World!" With Python
    """
    hello_world()

    want = "Hello, World!\n"
    got = capsys.readouterr().out
    assert got == want


def test_if_else(capsys: CaptureFixture[str]) -> None:
    """
    https://www.hackerrank.com/challenges/py-if-else/problem
    Python If-Else
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        name: str
        n: int
        want: str

    for i, tt in enumerate(
        (
            TestCase(name="홀수", n=1, want="Weird"),
            TestCase(name="홀수", n=3, want="Weird"),
            TestCase(name="홀수", n=5, want="Weird"),
            TestCase(name="홀수", n=21, want="Weird"),
            TestCase(name="2~5", n=2, want="Not Weird"),
            TestCase(name="2~5", n=4, want="Not Weird"),
            TestCase(name="6~20", n=6, want="Weird"),
            TestCase(name="6~20", n=20, want="Weird"),
            TestCase(name="greater than 20", n=22, want="Not Weird"),
        )
    ):
        if_else(tt.n)

        want = f"""{tt.want}
"""
        got = capsys.readouterr().out
        assert got == want, f"{i}/{tt.name}"


def test_loops(capsys: CaptureFixture[str]) -> None:
    """
    https://www.hackerrank.com/challenges/python-loops/problem
    Loops
    """
    loops(5)

    want = """0
1
4
9
16
"""
    got = capsys.readouterr().out
    assert got == want


def test_print_function(capsys: CaptureFixture[str]) -> None:
    """
    https://www.hackerrank.com/challenges/python-print/problem
    Print Function
    """
    print_function(3)

    want = """123
"""
    got = capsys.readouterr().out
    assert got == want


def test_is_leap() -> None:
    """
    https://www.hackerrank.com/challenges/write-a-function/problem
    Write a function
    :return:
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        year: int
        want: bool

    for tt in (
        TestCase(year=2000, want=True),
        TestCase(year=2400, want=True),
        TestCase(year=1800, want=False),
        TestCase(year=1900, want=False),
        TestCase(year=2100, want=False),
        TestCase(year=2200, want=False),
        TestCase(year=2300, want=False),
        TestCase(year=2500, want=False),
        TestCase(year=1, want=False),
        TestCase(year=4, want=True),
    ):
        got = is_leap(tt.year)
        assert got == tt.want
