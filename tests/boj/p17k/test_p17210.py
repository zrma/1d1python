from io import StringIO

import attrs

from src.boj.p17k.p17210 import solve17210


def test_solve17210() -> None:
    """
    https://www.acmicpc.net/problem/17210
    문문문
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        give: str
        want: str

    for i, tt in enumerate(
        (
            TestCase(
                give="""4
0""",
                want="""1
0
1""",
            ),
            TestCase(
                give="""5
0""",
                want="""1
0
1
0""",
            ),
            TestCase(
                give="""5
1""",
                want="""0
1
0
1""",
            ),
            TestCase(
                give="""10
1""",
                want="""Love is open door""",
            ),
        )
    ):
        reader = StringIO(tt.give)
        writer = StringIO()
        solve17210(reader, writer)

        got = writer.getvalue()
        assert got == tt.want, f"{i}/{tt}"
