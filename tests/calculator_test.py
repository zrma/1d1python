import unittest

from src.calculator import parse


class TestCalculator(unittest.TestCase):
    def setUp(self):
        pass

    def test_parse(self):
        self.assertEqual(parse("1 + 3"), ("+", 1, 3), "공백을 잘 처리한다")
        self.assertEqual(parse("1 * 3"), ("*", 1, 3))
        self.assertEqual(parse("1/ 3"), ("/", 1, 3))
        self.assertEqual(parse("1-3"), ("-", 1, 3), "공백이 없을 경우에도 파싱 성공한다.")
