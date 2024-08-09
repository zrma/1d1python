from io import StringIO

import attrs

from src.boj.p17k.p17618 import solve17618


def test_solve17618() -> None:
    """
    https://www.acmicpc.net/problem/17618
    신기한 수
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        give: str
        want: str

    for i, tt in enumerate(
        (
            TestCase(
                give="9",
                want="9",
            ),
            TestCase(
                give="10",
                want="10",
            ),
            TestCase(
                give="11",
                want="10",
            ),
            TestCase(
                give="21",
                want="14",
            ),
            TestCase(
                give="100000",
                want="11872",
            ),
        )
    ):
        reader = StringIO(tt.give)
        writer = StringIO()
        solve17618(reader, writer)

        got = writer.getvalue()
        assert got == tt.want, f"{i}/{tt}"
