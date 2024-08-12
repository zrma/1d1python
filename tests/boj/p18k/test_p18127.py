from io import StringIO

import attrs

from src.boj.p18k.p18127 import solve18127


def test_solve18127() -> None:
    """
    https://www.acmicpc.net/problem/18127
    모형결정
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        give: str
        want: str

    for i, tt in enumerate(
        (
            TestCase(
                give="3 0",
                want="1",
            ),
            TestCase(
                give="3 1",
                want="3",
            ),
            TestCase(
                give="3 2",
                want="6",
            ),
            TestCase(
                give="3 3",
                want="10",
            ),
            TestCase(
                give="3 4",
                want="15",
            ),
            TestCase(
                give="3 5",
                want="21",
            ),
            TestCase(
                give="4 0",
                want="1",
            ),
            TestCase(
                give="4 1",
                want="4",
            ),
            TestCase(
                give="4 2",
                want="9",
            ),
            TestCase(
                give="4 3",
                want="16",
            ),
            TestCase(
                give="4 4",
                want="25",
            ),
            TestCase(
                give="4 5",
                want="36",
            ),
            TestCase(
                give="5 0",
                want="1",
            ),
            TestCase(
                give="5 1",
                want="5",
            ),
            TestCase(
                give="5 2",
                want="12",
            ),
            TestCase(
                give="5 3",
                want="22",
            ),
            TestCase(
                give="5 4",
                want="35",
            ),
            TestCase(
                give="5 5",
                want="51",
            ),
            TestCase(
                give="6 0",
                want="1",
            ),
            TestCase(
                give="6 1",
                want="6",
            ),
            TestCase(
                give="6 2",
                want="15",
            ),
            TestCase(
                give="6 3",
                want="28",
            ),
            TestCase(
                give="6 4",
                want="45",
            ),
            TestCase(
                give="6 5",
                want="66",
            ),
            TestCase(
                give="7 0",
                want="1",
            ),
            TestCase(
                give="7 1",
                want="7",
            ),
            TestCase(
                give="7 2",
                want="18",
            ),
        )
    ):
        reader = StringIO(tt.give)
        writer = StringIO()
        solve18127(reader, writer)

        got = writer.getvalue()
        assert got == tt.want, f"{i}/{tt}"
