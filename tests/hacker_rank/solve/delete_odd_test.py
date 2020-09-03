from collections import namedtuple

from src.hacker_rank.solve.delete_odd import SinglyLinkedList
from src.hacker_rank.solve.delete_odd import delete_odd
from src.hacker_rank.solve.delete_odd import print_singly_linked_list

Case = namedtuple("TestCase", "data expected")


def test_frequency():
    cases = (
        Case(data=(2, 1, 3, 4, 6),
             expected="2 4 6"),
        Case(data=(1, 3, 2, 7, 10),
             expected="2 10"),
    )

    for case in cases:
        list_head = SinglyLinkedList()

        for num in case.data:
            list_head_item = num
            list_head.insert_node(list_head_item)

        res = delete_odd(list_head.head)
        actual = print_singly_linked_list(res)

        assert actual == case.expected
