from collections import namedtuple

from src.hacker_rank.algorithms.strings.super_reduced_string import super_reduced_string

Case = namedtuple("TestCase", "data expected")


def test_frequency():
    # noinspection SpellCheckingInspection
    cases = (
        Case(data="aaabccddd",  # noqa
             expected="abd"),
        Case(data="aa",  # noqa
             expected="Empty String"),
        Case(data="baab",  # noqa
             expected="Empty String"),
        Case(data="abab",  # noqa
             expected="abab"),
        Case(data="abccba",  # noqa
             expected="Empty String"),
        Case(data="",
             expected="Empty String"),
    )

    for case in cases:
        data, expected = case  # type: str, str
        assert super_reduced_string(data) == expected
