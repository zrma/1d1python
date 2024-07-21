from io import StringIO
from typing import Callable

import attrs
import pytest

from src.boj.p15k.p15667 import solve15667, solve15667_sqrt


@attrs.frozen(auto_attribs=True, kw_only=True)
class TestCase:
    __test__ = False
    give: str
    want: str


test_cases: tuple[TestCase, ...] = (
    TestCase(give="3", want="1"),  # 1 + 1 + 1
    TestCase(give="7", want="2"),  # 1 + 2 + 4
    TestCase(give="13", want="3"),  # 1 + 3 + 9
    TestCase(give="21", want="4"),  # 1 + 4 + 16
    TestCase(give="31", want="5"),  # 1 + 5 + 25
    TestCase(give="101", want="10"),  # 1 + 10 + 100
    TestCase(give="10101", want="100"),  # 1 + 100 + 10000
)

SolveFunction = Callable[[StringIO, StringIO], None]

solve_funcs: list[SolveFunction] = [solve15667, solve15667_sqrt]


@pytest.mark.parametrize("tc", test_cases)
@pytest.mark.parametrize("solve_func", solve_funcs)
def test_solve15667(tc: TestCase, solve_func: SolveFunction) -> None:
    """
    https://www.acmicpc.net/problem/15667
    2018 연세대학교 프로그래밍 경진대회
    """
    reader = StringIO(tc.give)
    writer = StringIO()
    solve_func(reader, writer)
    got = writer.getvalue()
    assert got == tc.want, f"{solve_func.__name__}({tc})"
