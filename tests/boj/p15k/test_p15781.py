from io import StringIO

import attrs

from src.boj.p15k.p15781 import solve15781


def test_solve15781() -> None:
    """
    https://www.acmicpc.net/problem/15781
    헬멧과 조끼
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        give: str
        want: str

    for i, tt in enumerate(
        (
            TestCase(
                give="""5 7
10 60 15 20 7
1 2 3 7 5 1 3""",
                want="67",
            ),
            TestCase(
                give="""2 3
1 1000000000
20 18 1000000000""",
                want="2000000000",
            ),
        )
    ):
        reader = StringIO(tt.give)
        writer = StringIO()
        solve15781(reader, writer)

        got = writer.getvalue()
        assert got == tt.want, f"{i}/{tt}"
