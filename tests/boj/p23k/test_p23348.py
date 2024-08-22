from io import StringIO

import attrs

from src.boj.p23k.p23348 import solve23348


def test_solve23348() -> None:
    """
    https://www.acmicpc.net/problem/23348
    스트릿 코딩 파이터
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        give: str
        want: str

    for i, tt in enumerate(
        (
            TestCase(
                give="""3 6 9
2
1 2 3
1 1 1
2 2 2
0 0 0
0 1 0
3 3 3""",
                want="96",
            ),
            TestCase(
                give="""1 2 3
3
1 1 1
1 1 1
1 1 1
0 0 0
0 0 0
0 0 0
1 1 1
0 0 0
0 0 0""",
                want="18",
            ),
        )
    ):
        reader = StringIO(tt.give)
        writer = StringIO()
        solve23348(reader, writer)

        got = writer.getvalue()
        assert got == tt.want, f"{i}/{tt}"
