"""Module with basic non-prior queue"""
from typing import Any

from data_structures.task1.mylinkedlist import LinkedList


class Queue:
    """Basic queue implementation"""

    def __init__(self):
        self._list = LinkedList()

    def enqueue(self, value) -> None:
        """
        Add item to the queue to end of the queue

        :param value: Value to be added
        :return: None
        """
        return self._list.append(value)

    def dequeue(self) -> Any:
        """
        Return first element of the queue if present

        :return: First element of the queue
        :rtype: Any
        """
        return self._list.rpop()
