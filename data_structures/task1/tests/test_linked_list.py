"""Module with linked list tests"""
import pytest

from data_structures.task1.mylinkedlist import LinkedList


@pytest.fixture(name="filled_linked_list")
def fixture_linked_list():
    """
    Mock list with some data
    """
    my_list = LinkedList()

    for i in range(5):
        my_list.append(i)

    return my_list


@pytest.fixture(name="empty_linked_list")
def fixture_empty_linked_list():
    """
    Mock empty linked list
    """
    return LinkedList()


@pytest.mark.parametrize("expected", [
    ([4, 3, 2]),
    ([4, 3]),
    ([4, 3, 2, 1, 0]),
    ([4, 3, 2, 1, 0, None]),
])
def test_linked_list_pop(filled_linked_list, expected):
    for expected_item in expected:
        assert filled_linked_list.pop() == expected_item


@pytest.mark.parametrize("expected", [
    ([i for i in range(5)] + [None]),
])
def test_linked_list_rpop(filled_linked_list, expected):
    for i in range(len(filled_linked_list)):
        assert filled_linked_list.rpop() == expected[i]


@pytest.mark.parametrize("item_list, length", [
    ([5, 2, 7, 4, 78, -1, "erw"], 0),
])
def test_linked_list_append(empty_linked_list, item_list, length):
    for item in item_list:
        empty_linked_list.append(item)
        assert empty_linked_list.tail.value == item


@pytest.mark.parametrize("test_index, expected", [
    (5, False),
    (4, True),
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


@pytest.mark.parametrize("test_list, expected", [
    ([i for i in range(0)], 0),
    ([i for i in range(5)], 3),
    ([i for i in range(10)], 8)
])
def test_linked_list_counter(test_list, expected):
    empty_linked_list = LinkedList()
    for item in test_list:
        empty_linked_list.append(item)

    if expected != 0:
        assert empty_linked_list.counter == expected + 2
    empty_linked_list.pop()
    empty_linked_list.pop()
    assert empty_linked_list.counter == expected


@pytest.mark.parametrize("test_list, counter", [
    ([i for i in range(10)], 10),
    ([i for i in range(2)], 2),
    ([i for i in range(0)], 0),
])
def test_linked_list_prepend(empty_linked_list, test_list, counter):
    for item in test_list:
        empty_linked_list.prepend(item)
        assert empty_linked_list.head.value == item
    assert empty_linked_list.counter == counter


@pytest.mark.parametrize("index_list, test_list, expected", [
    ([0, 0, 2, 3, 1, 3], [i for i in range(6)], [1, 4, 0, 5, 2, 3])
])
def test_linked_list_insert(empty_linked_list, index_list, test_list, expected):
    for index, item in zip(index_list, test_list):
        empty_linked_list.insert(index, item)

    assert empty_linked_list == expected


@pytest.mark.parametrize("test_index", [
    -1,
    -1.5,
    55
])
def test_linked_list_insert_wrong_index(empty_linked_list, test_index):
    with pytest.raises(IndexError):
        empty_linked_list.insert(test_index, 0)
