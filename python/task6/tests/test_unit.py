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
    """Contains tests with correct input"""
    assert to_test.even_odd(test_input) == expected


@pytest.mark.parametrize("test_input", [
    0.1, "2"
])
def test_even_odd_negative_input_wrong_type(test_input):
    """Contains tests with wrong parameters type"""
    with pytest.raises(TypeError):
        to_test.even_odd(test_input)
