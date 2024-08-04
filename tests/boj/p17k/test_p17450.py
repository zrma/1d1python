from io import StringIO

import attrs

from src.boj.p17k.p17450 import solve17450


def test_solve17450() -> None:
    """
    https://www.acmicpc.net/problem/17450
    과자 사기
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        give: str
        want: str

    for i, tt in enumerate(
        (
            TestCase(
                give="""8 5
6 6
7 5""",
                want="N",
            ),
            TestCase(
                give="""5 5
5 1
1 5""",
                want="U",
            ),
            TestCase(
                give="""500 10
451 10
452 10""",
                want="S",
            ),
            TestCase(
                give="""503 10
451 10
452 10""",
                want="N",
            ),
            TestCase(
                give="""503 10
452 10
501 10""",
                want="U",
            ),
        )
    ):
        reader = StringIO(tt.give)
        writer = StringIO()
        solve17450(reader, writer)

        got = writer.getvalue()
        assert got == tt.want, f"{i}/{tt}"
