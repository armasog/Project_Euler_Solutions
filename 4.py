import unittest

'''
Challenge:

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''


class TestSuite(unittest.TestCase):
    def test_is_palindrome(self):
        assert is_palindrome(1001) == True and is_palindrome(10001) == True and is_palindrome(
            1234) == False and is_palindrome(12345) == False

    def test_solution(self):
        assert solution(2) == 9009


def is_palindrome(number):
    number = str(number)
    number_of_digits = len(number)
    first_slice = int((number_of_digits / 2))
    first_slice_value = number[:first_slice]
    if number_of_digits % 2 == 0:
        second_slice_value = number[first_slice:]
    else:  # Important to exclude middle digit from consideration in numbers that have an odd number of digits
        second_slice_value = number[first_slice + 1:]
    if first_slice_value == second_slice_value[::-1]:
        return True
    return False


def solution(digits):
    lower_bound_factor = int('1' + '0' * (digits - 1))
    upper_bound_factor = int('9' * digits)
    largest_palindrome_product = 0
    factors = [i for i in range(lower_bound_factor, upper_bound_factor + 1)]
    for j in factors:
        for y in factors:
            if is_palindrome(j * y) and j * y > largest_palindrome_product:
                largest_palindrome_product = j * y
    return largest_palindrome_product


answer = solution(3)  # Answer evaluates to 906609
