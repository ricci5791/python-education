"""Module contains tests for code from to_test.py"""

import pytest

from python.task6 import to_test


@pytest.mark.parametrize("test_input, expected", [
    (2, "even"),
    (3, "odd"),
    (2e100, "even"),
    (-1, "odd"),
    (-2, "even"),
])
def test_even_odd_positive_input(test_input, expected):
    """Contains tests for 'even_odd' func with correct input"""
    assert to_test.even_odd(test_input) == expected


@pytest.mark.parametrize("test_input", [
    0.1, "2"
])
def test_even_odd_negative_input_wrong_type(test_input):
    """Contains tests for 'even_odd' func with wrong parameters type"""
    with pytest.raises(TypeError):
        to_test.even_odd(test_input)


@pytest.mark.parametrize("test_input, expected", [
    ([1, 2, 3, 4, 5], 15),
    ([2.1, 3.9, 4], 10.),
    ([1, 1e10], 10_000_000_001),
    ([5, -4, 3, -2, 1, 0, -1, 2], 4),
])
def test_sum_all_positive_input(test_input, expected):
    """Contains tests for 'sum_all' func with correct input"""
    assert to_test.sum_all(*test_input) == expected


@pytest.mark.parametrize("test_input", [
    ([1, 2, 3, "4"]),
    ([1, 2, 3, None]),
    ([None, None]),
])
def test_sum_all_negative_input_wrong_type(test_input):
    """Contains tests for 'sum_all' func with wrong parameters type"""
    with pytest.raises(TypeError):
        to_test.sum_all(*test_input)
