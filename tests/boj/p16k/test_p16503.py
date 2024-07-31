from io import StringIO

import attrs

from src.boj.p16k.p16503 import solve16503


def test_solve16503() -> None:
    """
    https://www.acmicpc.net/problem/16503
    괄호 없는 사칙연산
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        give: str
        want: str

    for i, tt in enumerate(
        (
            TestCase(
                give="""2 + 3 * 4""",
                want="""14
20""",
            ),
            TestCase(
                give="""6 / 2 * 3""",
                want="""1
9""",
            ),
            TestCase(
                give="""5 + 10 + 10""",
                want="""25
25""",
            ),
            TestCase(
                give="""7 / 3 - 9""",
                want="""-7
-1""",
            ),
        )
    ):
        reader = StringIO(tt.give)
        writer = StringIO()
        solve16503(reader, writer)

        got = writer.getvalue()
        assert got == tt.want, f"{i}/{tt}"
