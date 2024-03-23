import pytest

def is_even(number: int) -> bool:
   return number % 2 == 0

def test_is_even_test():
    expected_result = True
    actual_result = is_even(8)
    assert expected_result == actual_result


def test_is_even_not():
    expected_result = False
    actual_result = is_even(1)


