from io import StringIO

import attrs

from src.boj.p16k.p16673 import solve16673


def test_solve16673() -> None:
    """
    https://www.acmicpc.net/problem/16673
    고려대학교에는 공식 와인이 있다
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        give: str
        want: str

    for i, tt in enumerate(
        (
            TestCase(
                give="""3 1 1""",
                want="20",
            ),
            TestCase(
                give="""5 28 27""",
                want="1905",
            ),
        )
    ):
        reader = StringIO(tt.give)
        writer = StringIO()
        solve16673(reader, writer)

        got = writer.getvalue()
        assert got == tt.want, f"{i}/{tt}"
