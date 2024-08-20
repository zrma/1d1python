from io import StringIO

import attrs

from src.boj.p21k.p21866 import solve21866


def test_solve21866() -> None:
    """
    https://www.acmicpc.net/problem/21866
    추첨을 통해 커피를 받자
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        give: str
        want: str

    for i, tt in enumerate(
        (
            TestCase(
                give="100 0 0 0 0 0 0 0 0",
                want="draw",
            ),
            TestCase(
                give="0 50 0 0 0 0 0 0 0",
                want="none",
            ),
            TestCase(
                give="101 101 201 201 301 301 401 401 501",
                want="hacker",
            ),
        )
    ):
        reader = StringIO(tt.give)
        writer = StringIO()
        solve21866(reader, writer)

        got = writer.getvalue()
        assert got == tt.want, f"{i}/{tt}"
