from typing import Union


class SinglyLinkedListNode:
    def __init__(self, node_data: int):
        self.data: int = node_data
        self.next: Union[SinglyLinkedListNode, None] = None


class SinglyLinkedList:
    def __init__(self):
        self.head: Union[SinglyLinkedListNode, None] = None
        self.tail: Union[SinglyLinkedListNode, None] = None

    def insert_node(self, node_data: int):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        elif self.tail:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node: Union[SinglyLinkedListNode, None]):
    data = ""

    while node:
        data += str(node.data)
        node = node.next

        if node:
            data += " "

    return data


def delete_odd(list_head: SinglyLinkedListNode):
    new_list = SinglyLinkedList()

    current_node: Union[SinglyLinkedListNode, None] = list_head

    while current_node:
        current_data: int = current_node.data
        if current_data % 2 == 0:
            new_list.insert_node(current_data)

        current_node = current_node.next

    return new_list.head
