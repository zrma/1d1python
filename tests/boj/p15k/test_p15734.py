from io import StringIO

import attrs

from src.boj.p15k.p15734 import solve15734


def test_solve15734() -> None:
    """
    https://www.acmicpc.net/problem/15734
    명장 남정훈
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        give: str
        want: str

    for i, tt in enumerate(
        (
            TestCase(give="1 5 2", want="6"),
            TestCase(give="5 1 2", want="6"),
            TestCase(give="7 7 7", want="20"),
        )
    ):
        reader = StringIO(tt.give)
        writer = StringIO()
        solve15734(reader, writer)

        got = writer.getvalue()
        assert got == tt.want, f"{i}/{tt}"
