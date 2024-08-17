from io import StringIO

import attrs

from src.boj.p20k.p20053 import solve20053


def test_solve20053() -> None:
    """
    https://www.acmicpc.net/problem/20053
    Maximum, Minimum
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        give: str
        want: str

    for i, tt in enumerate(
        (
            TestCase(
                give="""3
5
20 28 22 25 21
5
30 21 17 25 29
5
20 10 35 30 7""",
                want="""20 28
17 30
7 35""",
            ),
            TestCase(
                give="""1
5
5 4 3 2 1""",
                want="""1 5""",
            ),
        )
    ):
        reader = StringIO(tt.give)
        writer = StringIO()
        solve20053(reader, writer)

        got = writer.getvalue()
        assert got == tt.want, f"{i}/{tt}"
