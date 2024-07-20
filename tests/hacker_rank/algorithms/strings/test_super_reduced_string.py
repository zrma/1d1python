import attrs

from src.hacker_rank.algorithms.strings.super_reduced_string import super_reduced_string


def test_frequency() -> None:
    """
    https://www.hackerrank.com/challenges/reduced-string/problem
    Super Reduced String
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        give: str
        want: str

    empty_string = "Empty String"

    test_cases = (
        TestCase(
            give="aaabccddd",  # noqa
            want="abd",
        ),
        TestCase(
            give="aa",  # noqa
            want=empty_string,
        ),
        TestCase(
            give="baab",  # noqa
            want=empty_string,
        ),
        TestCase(
            give="abab",  # noqa
            want="abab",
        ),
        TestCase(
            give="abccba",  # noqa
            want=empty_string,
        ),
        TestCase(give="", want=empty_string),
    )

    for tt in test_cases:
        got = super_reduced_string(tt.give)
        assert got == tt.want
