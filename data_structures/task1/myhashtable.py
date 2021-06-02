"""Module with hash table implementation"""

from data_structures.task1.mylinkedlist import LinkedList


class HashTable:
    """
    Contains hashtable implementation
    """
    LIST_LENGTH = 15

    def __init__(self):
        self._list = LinkedList()

        for _ in range(self.LIST_LENGTH):
            self._list.append(LinkedList())

    @staticmethod
    def _hash_key(key) -> int:
        """
        Hash key with simple 'str->int code' function

        :param key: Value to be hashed
        :return: Integer that correspond to the key
        :rtype: int
        """
        hash_code = 0

        for index, item in enumerate(str.encode(key, "utf-8")):
            hash_code += (item * (index + 1))
        return hash_code % HashTable.LIST_LENGTH

    def insert(self, key, value):
        """
        Inserts pair of (key, value) to the table

        :param key: Key to be searched for
        :param value: Data to stored
        :return: None
        """
        if not isinstance(key, str):
            raise TypeError

        index = self._hash_key(key)

        self._list[index].value.append(value)

    def lookup(self, key):
        """
        Return data stored with the given key

        :param key: Key to look up
        :return: List of elements that stored in this cell
        """
        index = self._hash_key(key)

        return self._list[index]

    def delete(self, key, value=None):
        """
        Delete elements stored with th given key

        :param key: Key of element to delete
        :param value: If there is multiple elements delete all of them if value=
        None, specific element otherwise
        :return: None
        """

        index = self._hash_key(key)

        if value is None:
            self._list.delete(index)

        value_index = self._list[index].value.lookup(value)

        self._list[index].value.delete(value_index)
