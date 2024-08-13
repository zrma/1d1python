from io import StringIO

import attrs

from src.boj.p18k.p18247 import solve18247


def test_solve18247() -> None:
    """
    https://www.acmicpc.net/problem/18247
    겨울왕국 티켓 예매
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        give: str
        want: str

    for i, tt in enumerate(
        (
            TestCase(
                give="""1
13 4""",
                want="""48""",
            ),
            TestCase(
                give="""2
13 5
10 9""",
                want="""59
-1""",
            ),
        )
    ):
        reader = StringIO(tt.give)
        writer = StringIO()
        solve18247(reader, writer)

        got = writer.getvalue()
        assert got == tt.want, f"{i}/{tt}"
