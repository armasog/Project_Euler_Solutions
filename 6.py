import unittest

'''
Challenge:

The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 55**2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

'''


class TestSuite(unittest.TestCase):
    def test_sum_of_squares(self):
        assert sum_of_squares(10) == 385

    def test_square_of_sum(self):
        assert square_of_sum(10) == 3025

    def test_solution(self):
        assert solution(10) == 2640


def sum_of_squares(upper_bound):
    result = 0
    for i in range(1, upper_bound + 1):
        result += i ** 2
    return result


def square_of_sum(upper_bound):
    result = 0
    for i in range(1, upper_bound + 1):
        result += i
    return result ** 2


def solution(upper_bound):
    return square_of_sum(upper_bound) - sum_of_squares(upper_bound)


answer = solution(100)  # Answer evaluates to 25164150
