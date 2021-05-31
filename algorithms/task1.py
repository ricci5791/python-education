"""Module with binary search, quick sort, factorial function"""
from typing import List


def binary_search(arr: List[int], value: int) -> int:
    """
    Binary search in integer list of values

    :param arr: Integer list of data
    :param value: Value to be looked for
    :return: Index of value if were found
    :rtype: int
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        pivot = (left + right) // 2
        if arr[pivot] < value:
            left = pivot + 1
        elif arr[pivot] > value:
            right = pivot - 1
        else:
            return pivot

    return -1
