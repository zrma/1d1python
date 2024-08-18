from io import StringIO

import attrs

from src.boj.p20k.p20361 import solve20361


def test_solve20361() -> None:
    """
    https://www.acmicpc.net/problem/20361
    일우는 야바위꾼
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        give: str
        want: str

    for i, tt in enumerate(
        (
            TestCase(
                give="""3 2 4
1 3
3 2
3 1
2 3""",
                want="1",
            ),
            TestCase(
                give="""4 1 4
1 2
2 3
3 4
1 2""",
                want="4",
            ),
        ),
    ):
        reader = StringIO(tt.give)
        writer = StringIO()
        solve20361(reader, writer)

        got = writer.getvalue()
        assert got == tt.want, f"{i}/{tt}"
