import unittest

from calculator.function import parse, calc


class TestCalculator(unittest.TestCase):
    def setUp(self):
        pass

    def test_parse(self):
        self.assertEqual(parse("1 + 3"), ("+", 1, 3), "공백을 잘 처리한다")
        self.assertEqual(parse("1 * 3"), ("*", 1, 3))
        self.assertEqual(parse("1/ 3"), ("/", 1, 3))
        self.assertEqual(parse("1-3"), ("-", 1, 3), "공백이 없을 경우에도 파싱 성공한다.")

    def test_calc(self):
        self.assertEqual(calc(("+", 1, 2)), 3)
        self.assertEqual(calc(("-", 1, 2)), -1)
        self.assertEqual(calc(("*", 1, 2)), 2)
        self.assertEqual(calc(("/", 1, 2)), 0.5)
        self.assertRaises(ZeroDivisionError, calc, ("/", 1, 0))
