from io import StringIO

import attrs

from src.boj.p21k.p21603 import solve21603


def test_solve21603() -> None:
    """
    https://www.acmicpc.net/problem/21603
    K 2K 게임
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        give: str
        want: str

    for i, tt in enumerate(
        (
            TestCase(
                give="9 4",
                want="""7
1 2 3 5 6 7 9""",
            ),
            TestCase(
                give="16 12",
                want="""12
1 3 5 6 7 8 9 10 11 13 15 16""",
            ),
            TestCase(
                give="1 1",
                want="0",
            ),
            TestCase(
                give="1 2",
                want="""1
1""",
            ),
        )
    ):
        reader = StringIO(tt.give)
        writer = StringIO()
        solve21603(reader, writer)

        got = writer.getvalue()
        assert got == tt.want, f"{i}/{tt}"
