""" Tests for quick sort algo"""
import pytest
import random
from algorithms.task1 import quick_sort, factorial, binary_search

from math import factorial as m_factorial


@pytest.mark.parametrize("test_input, expected", [
    (1, m_factorial(1)),
    (2, m_factorial(2)),
    (3, m_factorial(3)),
    (10, m_factorial(10)),
    (20, m_factorial(20)),
])
def test_factorial(test_input, expected):
    assert factorial(test_input) == expected


@pytest.mark.parametrize("test_list, item, expected", [
    ([i for i in range(20)], 5, [i for i in range(20)].index(5)),
    ([i * 2 for i in range(100)], 42, [i * 2 for i in range(100)].index(42)),
    ([i for i in range(10)], -1, -1),
])
def test_binary_search(test_list, item, expected):
    assert binary_search(test_list, item) == expected


def test_quick_sort():
    for i in [i for i in range(10)]:
        random.seed(i)
        test_list = [random.randint(0, 100) for _ in range(20)]
        expected = sorted(test_list)
        test_list = quick_sort(test_list)
        assert test_list == expected
