import unittest
from collections import namedtuple
from typing import List

from src.hacker_rank.solve.delete_odd import SinglyLinkedList
from src.hacker_rank.solve.delete_odd import delete_odd
from src.hacker_rank.solve.delete_odd import print_singly_linked_list

TestCase = namedtuple("TestCase", "input expected")


class TestDeleteOdd(unittest.TestCase):
    def setUp(self):
        pass

    def test_frequency(self):
        cases: List[TestCase] = [
            TestCase(input=[2, 1, 3, 4, 6],
                     expected="2 4 6"),
            TestCase(input=[1, 3, 2, 7, 10],
                     expected="2 10"),
        ]

        for case in cases:
            list_head = SinglyLinkedList()

            for num in case.input:
                list_head_item = num
                list_head.insert_node(list_head_item)

            res = delete_odd(list_head.head)
            actual = print_singly_linked_list(res)

            self.assertEqual(actual, case.expected)
