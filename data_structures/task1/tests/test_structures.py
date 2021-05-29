"""Tests for linked list implementation"""
import pytest

from data_structures.task1.myhashtable import HashTable
from data_structures.task1.mylinkedlist import LinkedList
from data_structures.task1.myqueue import Queue
from data_structures.task1.mystack import Stack


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


@pytest.fixture(name="filled_stack")
def fixture_stack():
    """
    Mock stack filled with some data
    """
    my_stack = Stack()

    for i in range(5):
        my_stack.push(i)

    return my_stack


@pytest.mark.parametrize("pop_counter, expected", [
    (3, [4, 3, 2]),
    (2, [4, 3]),
    (5, [4, 3, 2, 1, 0]),
    (6, [4, 3, 2, 1, 0, None]),
])
def test_linked_list_pop(filled_linked_list, pop_counter, expected):
    for expected_item in expected:
        assert filled_linked_list.pop() == expected_item


@pytest.mark.parametrize("test_list, expected", [
    ([i for i in range(0)], 0),
    ([i for i in range(5)], 3),
    ([i for i in range(10)], 8)
])
def test_linked_list_counter(test_list, expected):
    empty_linked_list = LinkedList()
    for item in test_list:
        empty_linked_list.append(item)

    empty_linked_list.pop()
    empty_linked_list.pop()
    assert empty_linked_list.counter == expected


@pytest.mark.parametrize("test_index, expected", [
    (5, False),
    (0, True),
    (2, True),
])
def test_linked_list_delete(filled_linked_list, test_index, expected):
    assert filled_linked_list.delete(test_index) == expected


@pytest.mark.parametrize("test_item, expected", [
    ([i for i in range(5)], [i for i in range(5)]),
    ([6, 10, -1, "6", None], [-1 for _ in range(5)])
])
def test_linked_list_lookup(filled_linked_list, test_item, expected):
    for item in zip(test_item, expected):
        assert filled_linked_list.lookup(item[0]) == item[1]


@pytest.mark.parametrize("pop_counter, expected", [
    (3, [0, 1, 2]),
    (2, [0, 1]),
    (5, [0, 1, 2, 3, 4]),
    (6, [0, 1, 2, 3, 4, None]),
])
def test_queue(filled_queue, pop_counter, expected):
    for expected_item in expected:
        assert filled_queue.dequeue() == expected_item


@pytest.mark.parametrize("expected", [
    ([i for i in range(4, 0, -1)])
])
def test_stack_pop(filled_stack, expected):
    for expected_item in expected:
        assert filled_stack.pop() == expected_item


@pytest.mark.parametrize("list_to_insert, expected", [
    ([8, 2, 3], [4, 3, 2, 8, 3, 2, 1, 0])
])
def test_stack_pop_insert_pop(filled_stack, list_to_insert, expected):
    assert filled_stack.pop() == expected[0]

    for item in list_to_insert:
        filled_stack.push(item)

    for expected_item in expected[1:]:
        assert filled_stack.pop() == expected_item


@pytest.mark.parametrize("key, expected", [
    ("test", 2)
])
def test_hashtable_hash_function(key, expected):
    hashtable = HashTable()
    assert hashtable._hash_key(key) == expected
