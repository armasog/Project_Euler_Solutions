import unittest

'''
Challenge:

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''


class TestSuite(unittest.TestCase):
    def test_solution(self):
        assert solution(10) == 2520


def solution(upper_bound):
    smallest_multiple = 1
    step = 1
    for i in range(2, upper_bound + 1):
        while smallest_multiple % i != 0:
            smallest_multiple += step  # For efficiency we increment each number by the smallest multiple of the
            # previous factor in the series so that we only need to test for divisibility of one number at a time
        step = smallest_multiple
    return smallest_multiple


answer = solution(20)  # Answer evaluates to 232792560
