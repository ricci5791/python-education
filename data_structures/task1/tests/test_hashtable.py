"""Module with hashtable tests"""
import pytest

from data_structures.task1.myhashtable import HashTable
from data_structures.task1.mylinkedlist import LinkedList


@pytest.fixture(name="empty_hashtable")
def fixture_hashtable():
    """
    Mocks empty hashtable
    """
    return HashTable()


@pytest.fixture(name="filled_hashtable")
def fixture_filled_hashtable():
    """
    Mocks hashtable with filled items from [0 to 5)
    :return:
    """
    my_hash = HashTable()

    for i in range(5):
        my_hash.insert(str(i), i)

    return my_hash


@pytest.fixture(name="duplicates_list")
def fixture_duplicates_linked_list():
    """
    Mocks list of duplicates in hashtable node
    """
    my_list = LinkedList()
    my_list.append(52)
    my_list.append(40)
    return my_list


@pytest.mark.parametrize("key, expected", [
    ("test", 2)
])
def test_hashtable_hash_function(key, expected):
    hashtable = HashTable()
    assert hashtable._hash_key(key) == expected


@pytest.mark.parametrize("test_data_tuple, expected_value", [
    (("test2", 10), 10),
    (("yest", 0), 0),
])
def test_hashtable_insert_lookup(empty_hashtable, test_data_tuple,
                                 expected_value):
    key, value = test_data_tuple

    empty_hashtable.insert(key, value)
    assert empty_hashtable.lookup(key).value[0].value == expected_value


@pytest.mark.parametrize("test_pairs", [
    [("cbst", 52),
     ("acst", 40)]
])
def test_hashtable_insert_lookup_duplicates(empty_hashtable, duplicates_list,
                                            test_pairs):
    for test_key, test_value in test_pairs:
        empty_hashtable.insert(test_key, test_value)
    assert empty_hashtable.lookup(test_pairs[0][0]).value == duplicates_list


@pytest.mark.parametrize("test_keys", [
    (str(i) for i in range(5))
])
def test_hashtable_delete(filled_hashtable, test_keys):
    for test_key in test_keys:
        filled_hashtable.delete(test_key)
        assert filled_hashtable.lookup(test_key).value == LinkedList()


@pytest.mark.parametrize("test_key", [
    None,
    1,
    1.2,
    [1, 2],
])
def test_hashtable_inconsistent_key_type(empty_hashtable, test_key):
    with pytest.raises(TypeError):
        empty_hashtable.insert(test_key)
