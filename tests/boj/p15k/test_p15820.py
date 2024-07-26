from io import StringIO

import attrs

from src.boj.p15k.p15820 import solve15820


def test_solve15820() -> None:
    """
    https://www.acmicpc.net/problem/15820
    맞았는데 왜 틀리죠?
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        give: str
        want: str

    for i, tt in enumerate(
        (
            TestCase(
                give="""2 0
1 1
-1 -1""",
                want="Accepted",
            ),
            TestCase(
                give="""2 0
1 1
-1 0""",
                want="Wrong Answer",
            ),
            TestCase(
                give="""2 3
1 1
-1 -1
10 10
2147483647 0
0 0""",
                want="Why Wrong!!!",
            ),
            TestCase(
                give="""2 3
1 1
-1 -1
10 10
2147483647 2147483647
-2147483647 -2147483647""",
                want="Accepted",
            ),
            TestCase(
                give="""2 3
1 1
-1 1
10 10
2147483647 2147483647
-2147483647 -2147483647""",
                want="Wrong Answer",
            ),
        )
    ):
        reader = StringIO(tt.give)
        writer = StringIO()
        solve15820(reader, writer)

        got = writer.getvalue()
        assert got == tt.want, f"{i}/{tt}"
