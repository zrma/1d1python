from io import StringIO

import attrs

from src.boj.p16k.p16504 import solve16504


def test_solve16504() -> None:
    """
    https://www.acmicpc.net/problem/16504
    종이접기
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        give: str
        want: str

    for i, tt in enumerate(
        (
            TestCase(
                give="""4
2 6 5 4
1 5 7 6
9 8 8 7
1 4 7 8""",
                want="88",
            ),
            TestCase(
                give="""2
1 2
3 4""",
                want="10",
            ),
        )
    ):
        reader = StringIO(tt.give)
        writer = StringIO()
        solve16504(reader, writer)

        got = writer.getvalue()
        assert got == tt.want, f"{i}/{tt}"
