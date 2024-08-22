from io import StringIO

import attrs

from src.boj.p23k.p23794 import solve23794


def test_solve23794() -> None:
    """
    https://www.acmicpc.net/problem/23794
    골뱅이 찍기 - 정사각형
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        give: str
        want: str

    for i, tt in enumerate(
        (
            TestCase(
                give="1",
                want="""@@@
@ @
@@@""",
            ),
            TestCase(
                give="3",
                want="""@@@@@
@   @
@   @
@   @
@@@@@""",
            ),
            TestCase(
                give="5",
                want="""@@@@@@@
@     @
@     @
@     @
@     @
@     @
@@@@@@@""",
            ),
        )
    ):
        reader = StringIO(tt.give)
        writer = StringIO()
        solve23794(reader, writer)

        got = writer.getvalue()
        assert got == tt.want, f"{i}/{tt}"
