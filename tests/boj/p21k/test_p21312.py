from io import StringIO

import attrs

from src.boj.p21k.p21312 import solve21312


def test_solve21312() -> None:
    """
    https://www.acmicpc.net/problem/21312
    홀짝 칵테일
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        give: str
        want: str

    for i, tt in enumerate(
        (
            TestCase(
                give="2 3 5",
                want="15",
            ),
            TestCase(
                give="11 33 99",
                want="35937",
            ),
            TestCase(
                give="22 44 88",
                want="85184",
            ),
        )
    ):
        reader = StringIO(tt.give)
        writer = StringIO()
        solve21312(reader, writer)

        got = writer.getvalue()
        assert got == tt.want, f"{i}/{tt}"
