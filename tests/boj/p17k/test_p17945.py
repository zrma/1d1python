from io import StringIO

import attrs

from src.boj.p17k.p17945 import solve17945


def test_solve17945() -> None:
    """
    https://www.acmicpc.net/problem/17945
    통학의 신
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        give: str
        want: str

    for i, tt in enumerate(
        (
            TestCase(
                give="2 3",
                want="-3 -1",
            ),
            TestCase(
                give="1 -8",
                want="-4 2",
            ),
            TestCase(
                give="1 1",
                want="-1",
            ),
        )
    ):
        reader = StringIO(tt.give)
        writer = StringIO()
        solve17945(reader, writer)

        got = writer.getvalue()
        assert got == tt.want, f"{i}/{tt}"
