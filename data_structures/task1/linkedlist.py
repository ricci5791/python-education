"""Contains implementation of linked list"""
from typing import Any


class LinkedList:
    """Implementation of one-way linked list"""

    class _Node:
        """Utility class that represents item in linked list"""

        def __init__(self, value: Any):
            self.next_node = None
            self.value = value

        def __str__(self):
            return str(self.value)

    def __init__(self):
        self.head = None
        self.tail = None
        self.counter = 0

    def append(self, value: Any):
        """
        Appends value to the end of the list

        :param value: Element to append
        :type value: Any
        :return: None
        """
        new_node = LinkedList._Node(value)

        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

        self.counter += 1

    def pop(self) -> Any:
        """
        Returns last element of the list and deletes it

        :return: Last value if present
        :rtype: Any
        """
        if not self.is_empty():
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

        return None

    def rpop(self) -> Any:
        """
        Pops first item of the list if exists

        :return: First element from the list
        :rtype: Any
        """
        if not self.is_empty():
            prev_head = self.head

            self.head = prev_head.next_node
            self.counter -= 1

            return prev_head.value

        return None

    def lookup(self, value: Any) -> bool:
        """
        Checks if given item in the list

        :param value:
        :return: Whether item in the list
        :rtype: bool
        """
        if not self.is_empty():
            for item in self:
                if item.value == value:
                    return True

        return False

    def is_empty(self) -> bool:
        """
        Checks if list is empty

        :return: True if list is empty, False otherwise
        :rtype: bool
        """

        return self.counter == 0

    def __repr__(self):
        res = ""

        for item in self:
            res += str(item.value) + ", "

        return res

    def __iter__(self):
        if not self.is_empty():
            curr_node = self.head

            while curr_node is not None:
                yield curr_node
                curr_node = curr_node.next_node
