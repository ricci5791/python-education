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

    def prepend(self, value):
        """
        Add element to the head of the list

        :param value: Data to store
        :return: None
        """
        temp_head = self.head

        self.head = LinkedList._Node(value)

        if not self.is_empty():
            self.head.next_node = temp_head
        else:
            self.tail = self.head

        self.counter += 1

    def insert(self, index, value):
        """
        Inserts value to the given index

        :param index:
        :param value:
        :return: None
        """
        if -1 < index <= self.counter:
            if index == 0:
                self.prepend(value)
            elif index == self.counter:
                self.append(value)
            else:
                counter = 0
                node = self.head

                while counter != index - 1:
                    node = node.next_node
                    counter += 1

                sub_nodes = node.next_node
                node.next_node = LinkedList._Node(value)
                node.next_node.next_node = sub_nodes

                self.counter += 1
        else:
            raise IndexError

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

    def delete(self, index: int) -> bool:
        """
        Deletes element with given index if exists

        :param index: Index of the element to be deleted
        :return: Is deletion successful
        """
        if not -1 < index < self.counter:
            return False
        elif index == 0:
            self.rpop()
            return True

        temp_counter = 0
        curr_node = self.head
        prev_node = None

        while temp_counter != index:
            prev_node = curr_node
            curr_node = curr_node.next_node
            temp_counter += 1

        if curr_node.next_node is None:
            prev_node.next_node = None
        else:
            prev_node.next_node = curr_node.next_node

        self.counter -= 1

        return True

    def lookup(self, value: Any) -> int:
        """
        Finds index of the given element

        :param value:
        :return: Index of the given element. -1 if not found
        :rtype: int
        """
        if not self.is_empty():
            counter = -1
            for item in self:
                counter += 1
                if item.value == value:
                    return counter

        return -1

    def is_empty(self) -> bool:
        """
        Checks if list is empty

        :return: True if list is empty, False otherwise
        :rtype: bool
        """

        return self.counter == 0

    def __len__(self):
        return self.counter

    def __repr__(self):
        res = ""

        for item in self:
            res += str(item) + ", "

        return res

    def __getitem__(self, index):
        if not 0 <= index < self.counter:
            raise IndexError

        counter = 0
        for item_value in self:
            if index == counter:
                return item_value
            counter += 1

    def __iter__(self):
        if not self.is_empty():
            curr_node = self.head

            while curr_node is not None:
                yield curr_node
                curr_node = curr_node.next_node

    def __eq__(self, other):
        for item, other_item in zip(self, other):
            if item.value != other_item:
                return False

        return True
