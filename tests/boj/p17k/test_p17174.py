from io import StringIO

import attrs

from src.boj.p17k.p17174 import solve17174


def test_solve17174() -> None:
    """
    https://www.acmicpc.net/problem/17174
    전체 계산 횟수
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        give: str
        want: str

    for i, tt in enumerate(
        (
            TestCase(
                give="""13 10""",
                want="14",
            ),
            TestCase(
                give="""100 8""",
                want="113",
            ),
            TestCase(
                give="""100 10""",
                want="111",
            ),
            TestCase(
                give="""100 100""",
                want="101",
            ),
            TestCase(
                give="""10 5""",
                want="12",
            ),
        )
    ):
        reader = StringIO(tt.give)
        writer = StringIO()
        solve17174(reader, writer)

        got = writer.getvalue()
        assert got == tt.want, f"{i}/{tt}"
