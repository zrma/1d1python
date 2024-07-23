from io import StringIO

import attrs

from src.boj.p15k.p15784 import solve15784


def test_solve15784() -> None:
    """
    https://www.acmicpc.net/problem/15784
    질투진서
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        give: str
        want: str

    for i, tt in enumerate(
        (
            TestCase(
                give="""5 3 2
10 2 3 24 4
21 4 5 12 1
24 52 4 2 2
2 4 3 2 32
1 4 32 2 4""",
                want="HAPPY",
            ),
            TestCase(
                give="""2 2 2
1 1
2 1""",
                want="ANGRY",
            ),
        )
    ):
        reader = StringIO(tt.give)
        writer = StringIO()
        solve15784(reader, writer)

        got = writer.getvalue()
        assert got == tt.want, f"{i}/{tt}"
