from io import StringIO

import attrs

from src.boj.p17k.p17496 import solve17496


def test_solve17496() -> None:
    """
    https://www.acmicpc.net/problem/17496
    스타후르츠
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        give: str
        want: str

    for i, tt in enumerate(
        (
            TestCase(
                give="""7 3 2 750""",
                want="3000",
            ),
            TestCase(
                give="""60 10 300 1000""",
                want="1500000",
            ),
        )
    ):
        reader = StringIO(tt.give)
        writer = StringIO()
        solve17496(reader, writer)

        got = writer.getvalue()
        assert got == tt.want, f"{i}/{tt}"
