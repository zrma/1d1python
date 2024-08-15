from io import StringIO

import attrs

from src.boj.p18k.p18856 import solve18856


def test_solve18856() -> None:
    """
    https://www.acmicpc.net/problem/18856
    피드백
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        give: str
        want: str

    for i, tt in enumerate(
        (
            TestCase(
                give="5",
                want="""5
1 2 3 4 997""",
            ),
            TestCase(
                give="10",
                want="""10
1 2 3 4 5 6 7 8 9 997""",
            ),
        )
    ):
        reader = StringIO(tt.give)
        writer = StringIO()
        solve18856(reader, writer)

        got = writer.getvalue()
        assert got == tt.want, f"{i}/{tt}"
