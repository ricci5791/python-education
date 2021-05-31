"""Module with binary search, quick sort, factorial function"""
import math
from typing import List, Tuple


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


def factorial(num: int) -> int:
    """
    Calculates factorial with recursive approach

    :param num: Number to be factorialized
    :return: Factorial of the given number
    :rtype: int
    """
    if num == 0:
        return 1
    return num * factorial(num - 1)


def partition(arr, left, right) -> int:
    """
    Swaps elements in the array by comparison with pivot element

    :param arr: Array to be 'sorted'
    :param left: left index of partition
    :param right: right index of partition
    """
    middle_element = arr[(left + right) // 2]
    temp_left = left
    temp_right = right

    while temp_left <= temp_right:
        while arr[temp_left] < middle_element:
            temp_left += 1
        while arr[temp_right] > middle_element:
            temp_right -= 1
        if temp_left >= temp_right:
            break
        else:
            arr[temp_left], arr[temp_right] = arr[temp_right], arr[temp_left]
            temp_left += 1
            temp_right -= 1
    return temp_right


def quick_sort(arr: List) -> List:
    """


    :param arr:
    :return:
    """
    stack: List[Tuple] = list()
    stack.append((0, len(arr) - 1))

    while len(stack) != 0:
        left, right = stack.pop()
        if right <= left:
            continue
        index = partition(arr, left, right)

        if index - left > right - index:
            stack.append((left, index))
            stack.append((index + 1, right))
        else:
            stack.append((index + 1, right))
            stack.append((left, index))

    return arr
