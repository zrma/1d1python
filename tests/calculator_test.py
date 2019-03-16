import unittest
from collections import namedtuple
from typing import List

from calculator.function import calc, add_bracket

TestCase_Calc = namedtuple("TestCase_Calc", "data desc")
TestCase_Bracket = namedtuple("TestCase_Bracket", "data expected desc")


class TestCalculator(unittest.TestCase):
    def setUp(self):
        pass

    def x_test_calc(self):
        cases: List[TestCase_Calc] = [
            TestCase_Calc(data="1", desc="단항 처리"),
            TestCase_Calc(data="3 + 5", desc="공백 처리"),
            TestCase_Calc(data="(3 + 5) * 5", desc="괄호를 잘 처리함"),
            TestCase_Calc(data="-2", desc="음수 처리 보장"),
            TestCase_Calc(data="1 / 2 + 3", desc="사칙 연산 순서 보장"),
            TestCase_Calc(data="-2 + 2 / 3", desc="사칙 연산 순서 보장(높은 순위 연산자가 뒤쪽에 있는 경우)"),
            TestCase_Calc(data="1/2+3", desc="나눗셈 처리를 잘 함"),
            TestCase_Calc(data="1/(2+3)*5", desc="복잡한 수식"),
            TestCase_Calc(data="1/(5+3*2)+6", desc="복잡한 내부 수식"),
        ]

        for case in cases:
            self.assertEqual(calc(case.data), eval(case.data), case.desc)

        self.assertRaises(ZeroDivisionError, calc, "1/0")

    def test_add_bracket(self):
        cases: List[TestCase_Bracket] = [
            TestCase_Bracket(data="(3 + 5)", expected="(3+5)", desc="공백 처리"),
            TestCase_Bracket(data="1", expected="(1)", desc="단항 처리"),
            TestCase_Bracket(data="-1", expected="(0-1)", desc="음수 처리"),
            TestCase_Bracket(data="(-1)", expected="(0-1)", desc="괄호 안 음수 처리"),
            TestCase_Bracket(data="3 + 5", expected="(3+5)", desc="외곽 괄호를 잘 붙임"),
            TestCase_Bracket(data="1/2+3", expected="((1/2)+3)", desc="사칙 연산 순서 보장"),
            TestCase_Bracket(data="2 + 3 * 5", expected="(2+(3*5))", desc="사칙 연산 순서 보장(높은 순위 연산자가 뒤쪽에 있는 경우)"),
            TestCase_Bracket(data="1/(2+3)*5", expected="((1/(2+3))*5)", desc="복잡한 수식"),
            TestCase_Bracket(data="1/(5+3*2)+6", expected="(1/(5+(3*2))+6)", desc="복잡한 내부 수식"),
        ]

        for case in cases:
            self.assertEqual(add_bracket(case.data), case.expected, case.desc)
