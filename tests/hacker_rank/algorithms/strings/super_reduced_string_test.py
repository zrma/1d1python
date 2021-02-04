from dataclasses import dataclass

from src.hacker_rank.algorithms.strings.super_reduced_string import super_reduced_string


def test_frequency():
    @dataclass
    class Case:
        data: str
        expected: str

    empty_string = "Empty String"
    # noinspection SpellCheckingInspection
    cases = (
        Case(data="aaabccddd",  # noqa
             expected="abd"),
        Case(data="aa",  # noqa
             expected=empty_string),
        Case(data="baab",  # noqa
             expected=empty_string),
        Case(data="abab",  # noqa
             expected="abab"),
        Case(data="abccba",  # noqa
             expected=empty_string),
        Case(data="",
             expected=empty_string),
    )

    for case in cases:
        assert super_reduced_string(case.data) == case.expected
