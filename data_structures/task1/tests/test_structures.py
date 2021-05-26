"""Tests for linked list implementation"""
from data_structures.task1.linkedlist import LinkedList  # , Queue
from data_structures.task1.queue import Queue
import pytest


@pytest.fixture(name="filled_linked_list")
def fixture_linked_list():
    """
    Mock list with some data
    """
    my_list = LinkedList()

    for i in range(5):
        my_list.append(i)

    return my_list


@pytest.fixture(name="filled_queue")
def fixture_queue():
    """
    Mock queue filled with some data
    """
    my_queue = Queue()

    for i in range(5):
        my_queue.enqueue(i)

    return my_queue


@pytest.mark.parametrize("pop_counter, expected", [
    (3, [4, 3, 2]),
    (2, [4, 3]),
    (5, [4, 3, 2, 1, 0]),
    (6, [4, 3, 2, 1, 0, None]),
])
def test_linked_list_pop(filled_linked_list, pop_counter, expected):
    for expected_item in expected:
        assert filled_linked_list.pop() == expected_item


@pytest.mark.parametrize("pop_counter, expected", [
    (3, [0, 1, 2]),
    (2, [0, 1]),
    (5, [0, 1, 2, 3, 4]),
    (6, [0, 1, 2, 3, 4, None]),
])
def test_queue(filled_queue, pop_counter, expected):
    for expected_item in expected:
        assert filled_queue.dequeue() == expected_item
