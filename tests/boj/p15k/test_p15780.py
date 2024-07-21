from io import StringIO

import attrs

from src.boj.p15k.p15780 import solve15780


def test_solve15780() -> None:
    """
    https://www.acmicpc.net/problem/15780
    멀티탭 충분하니?
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        give: str
        want: str

    for i, tt in enumerate(
        (
            TestCase(
                give="""3 5
3 4 5 6 7""",
                want="YES",
            ),
            TestCase(
                give="""6 2
3 4""",
                want="NO",
            ),
            TestCase(
                give="""2 1
3""",
                want="YES",
            ),
            TestCase(
                give="""3 1
3""",
                want="NO",
            ),
            TestCase(
                give="""2 1
2""",
                want="NO",
            ),
            TestCase(
                give="""3 1
4""",
                want="NO",
            ),
            TestCase(
                give="""3 1
5""",
                want="YES",
            ),
        )
    ):
        reader = StringIO(tt.give)
        writer = StringIO()
        solve15780(reader, writer)

        got = writer.getvalue()
        assert got == tt.want, f"{i}/{tt}"
