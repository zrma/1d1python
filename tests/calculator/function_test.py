import unittest
from collections import namedtuple
from typing import List

from src.calculator.function import calc, parse, get_inner_bracket

TestCase_Calc = namedtuple("TestCase_Calc", "data desc")
TestCase_InnerBracket = namedtuple("TestCase_Pop", "data expected desc")
TestCase_Parse = namedtuple("TestCase_Parse", "data expected desc")


class TestFunction(unittest.TestCase):
    def setUp(self):
        pass

    def x_test_calc(self):
        cases: List[TestCase_Calc] = [
            TestCase_Calc(data="1", desc="단항 처리"),
            TestCase_Calc(data="3 + 5", desc="공백 처리"),
            TestCase_Calc(data="(3 + 5) * 5", desc="괄호를 잘 처리함"),
            TestCase_Calc(data="-2", desc="음수 처리 보장"),
            TestCase_Calc(data="0 + 3", desc="시작하는 0 누락 안 함"),
            TestCase_Calc(data="3 + 0", desc="끝나는 0 누락 안 함"),
            TestCase_Calc(data="1 + 0 + 2", desc="중간 0 누락 안 함"),
            TestCase_Calc(data="1 / 2 + 3", desc="사칙 연산 순서 보장"),
            TestCase_Calc(data="-2 + 2 / 3",
                          desc="사칙 연산 순서 보장(높은 순위 연산자가 뒤쪽에 있는 경우)"),
            TestCase_Calc(data="1/2+3", desc="나눗셈 처리를 잘 함"),
            TestCase_Calc(data="1/(2+3)*5", desc="복잡한 수식"),
            TestCase_Calc(data="1/(5+3*2)+6", desc="복잡한 내부 수식"),
        ]

        for case in cases:
            self.assertEqual(calc(case.data), eval(case.data), case.desc)

        self.assertRaises(ZeroDivisionError, calc, "1/0")

    def test_get_inner_bracket(self):
        cases: List[TestCase_InnerBracket] = [
            TestCase_InnerBracket(data=[1, "+", 2], expected=[1, "+", 2],
                                  desc="괄호가 없는 수식"),
            TestCase_InnerBracket(data=[1, "+", "(", 3, "+", 5, ")", "-", 2],
                                  expected=[3, "+", 5],
                                  desc="괄호가 한 쌍 있는 수식"),
            TestCase_InnerBracket(data=[4, "*", "(", 1, "+",
                                        "(", 3, "+", 5, ")",
                                        "-", 2, ")", "/", 3],
                                  expected=[3, "+", 5], desc=""),
        ]

        for case in cases:
            self.assertEqual(get_inner_bracket(case.data),
                             case.expected,
                             case.desc)

    def test_parse(self):
        cases: List[TestCase_Parse] = [
            TestCase_Parse(data="3 + 5", expected=[3, "+", 5], desc="공백 처리"),
            TestCase_Parse(data="1", expected=[1], desc="단항 처리"),
            TestCase_Parse(data="0", expected=[0], desc="단항 처리(0)"),
            TestCase_Parse(data="123", expected=[123], desc="여러 자릿수의 단항 처리"),
            TestCase_Parse(data="-1", expected=["-", 1], desc="음수 처리"),
            TestCase_Parse(data="(-1)", expected=["(", "-", 1, ")"],
                           desc="괄호 안 음수 처리"),
            TestCase_Parse(data="3 + 5", expected=[3, "+", 5],
                           desc="외곽 괄호를 잘 붙임"),
            TestCase_Parse(data="0 + 3", expected=[0, "+", 3],
                           desc="시작하는 0 누락 안 함"),
            TestCase_Parse(data="3 + 0", expected=[3, "+", 0],
                           desc="끝나는 0 누락 안 함"),
            TestCase_Parse(data="1 + 0 + 2", expected=[1, "+", 0, "+", 2],
                           desc="중간 0 누락 안 함"),
            TestCase_Parse(data="1/2+3", expected=[1, "/", 2, "+", 3],
                           desc="사칙 연산 순서 보장"),
            TestCase_Parse(data="20 + 3 * 5", expected=[20, "+", 3, "*", 5],
                           desc="사칙 연산 순서 보장(높은 순위 연산자가 뒤쪽에 있는 경우)"),
            TestCase_Parse(data="1/(2+3)*5",
                           expected=[1, "/", "(", 2, "+", 3, ")", "*", 5],
                           desc="복잡한 수식"),
            TestCase_Parse(data="1/(5+3*20)+6",
                           expected=[
                               1, "/", "(", 5, "+", 3, "*", 20, ")", "+", 6
                           ],
                           desc="복잡한 내부 수식"),
        ]

        for case in cases:
            self.assertEqual(parse(case.data), case.expected, case.desc)
