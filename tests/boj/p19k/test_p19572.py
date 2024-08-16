from io import StringIO

import attrs

from src.boj.p19k.p19572 import solve19572


def test_solve19572() -> None:
    """
    https://www.acmicpc.net/problem/19572
    가뭄(Small)
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        give: str
        want: str

    for i, tt in enumerate(
        (
            TestCase(
                give="4 4 4",
                want="""1
2.0 2.0 2.0""",
            ),
            TestCase(
                give="1 2 3",
                want="-1",
            ),
            TestCase(
                give="1 2 5",
                want="-1",
            ),
            TestCase(
                give="5 8 6",
                want="""1
3.5 1.5 4.5""",
            ),
        )
    ):
        reader = StringIO(tt.give)
        writer = StringIO()
        solve19572(reader, writer)

        got = writer.getvalue()
        assert got == tt.want, f"{i}/{tt}"
