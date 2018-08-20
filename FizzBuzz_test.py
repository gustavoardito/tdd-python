import unittest
from FizzBuzz import fizz_buzz


def test_can_call_fizz_buzz():
    fizz_buzz(1)


def test_return_1_for_1():
    return_value = fizz_buzz(1)
    assert return_value == '1'


def test_return_2_for_2():
    return_value = fizz_buzz(2)
    assert return_value == '2'


def test_return_fizz_for_3():
    return_value = fizz_buzz(3)
    assert return_value == 'Fizz'


def test_return_buzz_for_5():
    return_value = fizz_buzz(5)
    assert return_value == 'Buzz'


def test_return_fizz_for_6():
    return_value = fizz_buzz(6)
    assert return_value == 'Fizz'


def test_return_buzz_for_10():
    return_value = fizz_buzz(10)
    assert return_value == 'Buzz'


def test_return_fizz_buzz_for_15():
    return_value = fizz_buzz(15)
    assert return_value == 'FizzBuzz'
