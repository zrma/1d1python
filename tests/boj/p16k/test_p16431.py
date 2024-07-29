from io import StringIO

import attrs

from src.boj.p16k.p16431 import solve16431


def test_solve16431() -> None:
    """
    https://www.acmicpc.net/problem/16431
    베시와 데이지
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        give: str
        want: str

    for i, tt in enumerate(
        (
            TestCase(
                give="""3 5
1 1
2 3""",
                want="bessie",
            ),
            TestCase(
                give="""13 13
11 11
11 12""",
                want="daisy",
            ),
            TestCase(
                give="""4 5
5 4
4 4""",
                want="tie",
            ),
        )
    ):
        reader = StringIO(tt.give)
        writer = StringIO()
        solve16431(reader, writer)

        got = writer.getvalue()
        assert got == tt.want, f"{i}/{tt}"
