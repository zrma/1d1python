from io import StringIO

import attrs

from src.boj.p15k.p15921 import solve15921


def test_solve15921() -> None:
    """
    https://www.acmicpc.net/problem/15921
    수찬은 마린보이야!!
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        give: str
        want: str

    for i, tt in enumerate(
        (
            TestCase(
                give="""5
5 10 10 15 20""",
                want="1.00",
            ),
            TestCase(
                give="""5
0 0 0 0 0""",
                want="divide by zero",
            ),
            TestCase(
                give="""0""",
                want="divide by zero",
            ),
        )
    ):
        reader = StringIO(tt.give)
        writer = StringIO()
        solve15921(reader, writer)

        got = writer.getvalue()
        assert got == tt.want, f"{i}/{tt}"
