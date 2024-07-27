from io import StringIO

import attrs

from src.boj.p15k.p15917 import solve15917


def test_solve15917() -> None:
    """
    https://www.acmicpc.net/problem/15917
    노솔브 방지문제야!!
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        give: str
        want: str

    for i, tt in enumerate(
        (
            TestCase(
                give="""10
1
2
7
4
14
32
33
34
35
36""",
                want="""1
1
0
1
0
1
0
0
0
0""",
            ),
        )
    ):
        reader = StringIO(tt.give)
        writer = StringIO()
        solve15917(reader, writer)

        got = writer.getvalue()
        assert got == tt.want, f"{i}/{tt}"
