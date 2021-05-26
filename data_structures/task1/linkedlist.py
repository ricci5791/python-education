"""Contains implementation of linked list"""
from typing import Any


class LinkedList:
    """Implementation of one-way linked list"""

    class _Node:
        """Utility class that represents item in linked list"""

        def __init__(self, value: Any):
            self.next_node = None
            self.value = value

    def __init__(self):
        self.head = None
        self.tail = None
        self.counter = 0

    def append(self, value: Any):
        """Appends value to the end of the list"""
        new_node = LinkedList._Node(value)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

        self.counter += 1

    def pop(self):
        """Returns last element of the list and deletes it"""
        if self.counter == 0:
            return

        curr_node = self.head
        prev_node = None

        if self.counter == 1:
            self.head = None
            self.tail = None

            self.counter -= 1
            return curr_node.value

        if curr_node is not None:
            while curr_node.next_node is not None:
                prev_node = curr_node
                curr_node = curr_node.next_node

            prev_node.next_node = None
            self.tail = prev_node

            self.counter -= 1
            return curr_node.value
