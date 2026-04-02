"""
unit tests for calculator functions
"""

# import pytest
from calculator import get_numbers, add_numbers, multiply_numbers
from unittest.mock import patch


def test_add_numbers_positive():
    """"Test addition with positive numbers."""
    assert add_numbers([1, 2, 3]) == 6
    assert add_numbers([10, 20]) == 30


def test_add_numbers_negative():
    """"Addition with negative numbers."""
    assert add_numbers([-1, -2, -3]) == -6
    assert add_numbers([10, -5]) == 5


def test_add_numbers_single():
    """"Test addition with single number"""
    assert add_numbers([5]) == 5


def test_add_numbers_empty():
    """"Test addition with empty list."""
    assert add_numbers([]) == 0


def test_multiply_numbers_postive():
    """ Test multiplication with postive numbers"""
    assert multiply_numbers([2, 3, 4]) == 24
    assert multiply_numbers([5, 2]) == 10


def test_multiply_numbers_with_zero():
    """ Test multiplication with zero """
    assert multiply_numbers([3, 0, 20]) == 0


def test_multiply_numbers_single():
    """Test multiplication with a single number """
    assert multiply_numbers([3]) == 3


def test_multiply_numbers_with_negative_numbers():
    """Test multiplication with negatives """
    assert multiply_numbers([3, -3, 1]) == -9


@patch('builtins.input', side_effect=['5', '10', 'done'])
def test_get_numbers_valid(mock_input):
    """test getting valid number from user"""
    result = get_numbers()
    assert result == [5.0, 10.0]


@patch('builtins.input', side_effect=['5', 'abc', '10', 'done'])
def test_get_numbers_invalid(mock_input):
    """test getting numbers with invalid input"""
    result = get_numbers()
    assert result == [5.0, 10.0]
