"""Module contains stack linked list based implementation"""
from typing import Any

from data_structures.task1.mylinkedlist import LinkedList


class Stack:
    """Basic stack implementation"""

    def __init__(self):
        self._list = LinkedList()

    def push(self, value: Any):
        """
        Push given element to the stack

        :param value: Value to add
        :return: None
        """
        self._list.append(value)

    def pop(self) -> Any:
        """
        Pop top element from the stack

        :return: Value from the top
        :rtype: Any
        """
        return self._list.pop()

    def peek(self) -> Any:
        """
        Takes value from the top without deleting

        :return: Value from the top, None if empty
        :rtype: Any
        """
        if self._list.tail is None:
            return None
        return self._list.tail.value

    def __iter__(self):
        return iter(self._list)
