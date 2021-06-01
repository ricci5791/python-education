"""Module with stack tests"""
import pytest

from data_structures.task1.mystack import Stack


@pytest.fixture(name="filled_stack")
def fixture_stack():
    """
    Mock stack filled with some data
    """
    my_stack = Stack()

    for i in range(5):
        my_stack.push(i)

    return my_stack


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


@pytest.mark.parametrize("expected", [
    ([i for i in range(4, -1, -1)])
])
def test_stack_peek(filled_stack, expected):
    for item in expected:
        assert item == filled_stack.peek()
        filled_stack.pop()

    assert filled_stack.peek() is None
