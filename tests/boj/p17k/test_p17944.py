from io import StringIO

import attrs

from src.boj.p17k.p17944 import solve17944


def test_solve17944() -> None:
    """
    https://www.acmicpc.net/problem/17944
    퐁당퐁당 1
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        give: str
        want: str

    for i, tt in enumerate(
        (
            TestCase(
                give="""4 1""",
                want="1",
            ),
            TestCase(
                give="""4 3""",
                want="3",
            ),
            TestCase(
                give="""4 4""",
                want="4",
            ),
            TestCase(
                give="""4 7""",
                want="7",
            ),
            TestCase(
                give="""4 8""",
                want="8",
            ),
            TestCase(
                give="""4 9""",
                want="7",
            ),
            TestCase(
                give="""4 10""",
                want="6",
            ),
            TestCase(
                give="""4 11""",
                want="5",
            ),
            TestCase(
                give="""4 12""",
                want="4",
            ),
            TestCase(
                give="""4 13""",
                want="3",
            ),
            TestCase(
                give="""4 14""",
                want="2",
            ),
            TestCase(
                give="""4 15""",
                want="1",
            ),
            TestCase(
                give="""4 16""",
                want="2",
            ),
            TestCase(
                give="""3 7""",
                want="5",
            ),
            TestCase(
                give="""3 8""",
                want="4",
            ),
            TestCase(
                give="""3 11""",
                want="1",
            ),
            TestCase(
                give="""3 12""",
                want="2",
            ),
            TestCase(
                give="""3 16""",
                want="6",
            ),
            TestCase(
                give="""3 17""",
                want="5",
            ),
            TestCase(
                give="""3 21""",
                want="1",
            ),
            TestCase(
                give="""3 22""",
                want="2",
            ),
            TestCase(
                give="""5 18""",
                want="2",
            ),
            TestCase(
                give="""5 36""",
                want="2",
            ),
            TestCase(
                give="""1000 1000000""",
                want="500",
            ),
        )
    ):
        reader = StringIO(tt.give)
        writer = StringIO()
        solve17944(reader, writer)

        got = writer.getvalue()
        assert got == tt.want, f"{i}/{tt}"
