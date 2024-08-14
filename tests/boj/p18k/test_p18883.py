from io import StringIO

import attrs

from src.boj.p18k.p18883 import solve18883


def test_solve18883() -> None:
    """
    https://www.acmicpc.net/problem/18883
    N M 찍기
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        give: str
        want: str

    for i, tt in enumerate(
        (
            TestCase(
                give="3 4",
                want="""1 2 3 4
5 6 7 8
9 10 11 12
""",
            ),
            TestCase(
                give="1 2",
                want="""1 2
""",
            ),
        )
    ):
        reader = StringIO(tt.give)
        writer = StringIO()
        solve18883(reader, writer)

        got = writer.getvalue()
        assert got == tt.want, f"{i}/{tt}"
