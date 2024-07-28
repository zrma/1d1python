from io import StringIO

import attrs

from src.boj.p15k.p15953 import solve15953


def test_solve15953() -> None:
    """
    https://www.acmicpc.net/problem/15953
    상금 헌터
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        give: str
        want: str

    for i, tt in enumerate(
        (
            TestCase(
                give="""6
8 4
13 19
8 10
18 18
8 25
13 16""",
                want="""1780000
620000
1140000
420000
820000
620000""",
            ),
            TestCase(
                give="""2
0 0
1 1""",
                want="""0
10120000""",
            ),
        )
    ):
        reader = StringIO(tt.give)
        writer = StringIO()
        solve15953(reader, writer)

        got = writer.getvalue()
        assert got == tt.want, f"{i}/{tt}"
