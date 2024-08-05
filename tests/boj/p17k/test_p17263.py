from io import StringIO

import attrs

from src.boj.p17k.p17263 import solve17263


def test_solve17263() -> None:
    """
    https://www.acmicpc.net/problem/17263
    Sort 마스터
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        give: str
        want: str

    for i, tt in enumerate(
        (
            TestCase(
                give="""3
3 2 1""",
                want="3",
            ),
            TestCase(
                give="""5
5 5 5 5 5""",
                want="5",
            ),
            TestCase(
                give="""5
5 3 2 4 1""",
                want="5",
            ),
        )
    ):
        reader = StringIO(tt.give)
        writer = StringIO()
        solve17263(reader, writer)

        got = writer.getvalue()
        assert got == tt.want, f"{i}/{tt}"
