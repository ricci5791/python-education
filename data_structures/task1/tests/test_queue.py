"""Module with queue tests"""
import pytest

from data_structures.task1.myqueue import Queue


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
    (3, [0, 1, 2]),
    (2, [0, 1]),
    (5, [0, 1, 2, 3, 4]),
    (6, [0, 1, 2, 3, 4, None]),
])
def test_queue(filled_queue, pop_counter, expected):
    for expected_item in expected:
        assert filled_queue.dequeue() == expected_item
