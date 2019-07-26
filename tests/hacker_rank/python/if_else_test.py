from collections import namedtuple

from src.hacker_rank.python.if_else import if_else

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
