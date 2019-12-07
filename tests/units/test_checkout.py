import pytest
from pytest import raises
from unittest.mock import MagicMock
from Checkout.checkout import Checkout


@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.add_item_price('a', 1)
    checkout.add_item_price('b', 2)

    return checkout


@pytest.fixture()
def mock_open(monkeypatch):
    def get_rows():
        return ['A;13']
    mock_file = MagicMock()
    mock_file.readlines = MagicMock(side_effect=get_rows)
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr('builtins.open', mock_open)
    return mock_open


def test_return_correct_prices(checkout, mock_open, monkeypatch):
    mock_exists = MagicMock(return_value=True)
    monkeypatch.setattr('os.path.exists', mock_exists)
    result = checkout.get_prices('asdf')
    mock_open.assert_called_once_with('asdf', 'r')
    assert result == {'A': 13}


def test_throw_exception_with_bad_file(mock_open, monkeypatch):
    mock_exists = MagicMock(return_value=False)
    monkeypatch.setattr('os.path.exists', mock_exists)
    with raises(Exception):
        checkout.get_prices('asdf')


def test_can_calculate_total(checkout):
    checkout.add_item('a')
    assert checkout.calculate_total() == 1


def test_get_correct_total_with_multiple_items(checkout):
    checkout.add_item('a')
    checkout.add_item('b')
    assert checkout.calculate_total() == 3


def test_can_add_discount_rule(checkout):
    checkout.add_discount('a', 3, 2)


def test_can_apply_discount_rule(checkout):
    checkout.add_discount('a', 3, 2)
    checkout.add_item('a')
    checkout.add_item('a')
    checkout.add_item('a')
    assert checkout.calculate_total() == 2


def test_exception_with_bad_item(checkout):
    with pytest.raises(Exception):
        checkout.add_item('c')
