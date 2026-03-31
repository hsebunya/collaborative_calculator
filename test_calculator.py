"""
unit tests for calculator functions
"""

# import pytest
from calculator import get_numbers
from unittest.mock import patch


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
