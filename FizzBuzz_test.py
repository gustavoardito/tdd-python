import unittest
from FizzBuzz import fizz_buzz


def _validate_fizz_buzz(value, expected):
    return_value = fizz_buzz(value)
    assert return_value == expected


def test_return_1_for_1():
    _validate_fizz_buzz(1, '1')



def test_return_2_for_2():
    _validate_fizz_buzz(2, '2')


def test_return_fizz_for_3():
    _validate_fizz_buzz(3, 'Fizz')


def test_return_buzz_for_5():
    _validate_fizz_buzz(5, 'Buzz')


def test_return_fizz_for_6():
    _validate_fizz_buzz(6, 'Fizz')


def test_return_buzz_for_10():
    _validate_fizz_buzz(10, 'Buzz')


def test_return_fizz_buzz_for_15():
    return_value = fizz_buzz(15)
    assert return_value == 'FizzBuzz'
