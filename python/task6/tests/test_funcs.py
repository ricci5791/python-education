"""Module contains tests for functions from to_test.py"""

from unittest.mock import patch, Mock
import datetime as dt
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
    ([True, False]),
])
def test_sum_all_negative_input_wrong_type(test_input):
    """Contains tests for 'sum_all' func with wrong parameters type"""
    with pytest.raises(TypeError):
        to_test.sum_all(*test_input)


@pytest.mark.parametrize("test_hour, expected", [
    (0, "night"),
    (8, "morning"),
    (6, "morning"),
    (12, "afternoon"),
    (19, "night"),
])
def test_time_of_day(test_hour, expected):
    """Mocks datetime.now() and tests if statements in 'time_of_day' function"""
    datetime = Mock()
    datetime.now.return_value = dt.datetime.strptime(
            f"{test_hour}:20:19 20/05/21", '%H:%M:%S %d/%m/%y')

    with patch("python.task6.to_test.datetime", datetime):
        assert to_test.time_of_day() == expected
