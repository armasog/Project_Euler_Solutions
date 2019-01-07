import unittest

'''
Challenge:

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''


class TestSuite(unittest.TestCase):
    def test_factorial(self):
        assert factorial(10) == 3628800

    def test_solution(self):
        assert solution(3628800) == 27


def factorial(num):
    result = 1
    for i in range(num, 0, -1):
        result *= i
    return result


def solution(num):
    sum = 0
    string = str(num)
    for digit in string:
        sum += int(digit)
    return sum


answer = solution(factorial(100))  # Answer evaluates to 648
