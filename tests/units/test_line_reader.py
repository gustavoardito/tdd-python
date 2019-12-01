import pytest
from unittest.mock import MagicMock
from Doubles.line_reader import read_from_file


def test_return_correct_string(monkeypatch):
    mock_file = MagicMock()
    mock_file.readline = MagicMock(return_value='test line')
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr('builtins.open', mock_open)
    result = read_from_file('asdf')
    mock_open.assert_called_once_with('asdf', 'r')
    assert result == 'test line'
