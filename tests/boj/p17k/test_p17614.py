from io import StringIO

import attrs

from src.boj.p17k.p17614 import solve17614


def test_solve17614() -> None:
    """
    https://www.acmicpc.net/problem/17614
    369
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        give: str
        want: str

    for i, tt in enumerate(
        (
            TestCase(
                give="1",
                want="0",
            ),
            TestCase(
                give="2",
                want="0",
            ),
            TestCase(
                give="3",
                want="1",
            ),
            TestCase(
                give="4",
                want="1",
            ),
            TestCase(
                give="5",
                want="1",
            ),
            TestCase(
                give="6",
                want="2",
            ),
            TestCase(
                give="7",
                want="2",
            ),
            TestCase(
                give="8",
                want="2",
            ),
            TestCase(
                give="9",
                want="3",
            ),
            TestCase(
                give="14",
                want="4",
            ),
            TestCase(
                give="36",
                want="18",
            ),
        )
    ):
        reader = StringIO(tt.give)
        writer = StringIO()
        solve17614(reader, writer)

        got = writer.getvalue()
        assert got == tt.want, f"{i}/{tt}"
