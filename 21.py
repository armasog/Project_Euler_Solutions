import unittest
from functools import lru_cache

'''
Challenge:

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

'''


class TestSuite(unittest.TestCase):
    def test_sum_of_divisors(self):
        assert sum_of_divisors(220) == 284


@lru_cache(None)  # Optimizes run-time by caching previously calculated values of function
def sum_of_divisors(num):
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            if i not in divisors:
                divisors.append(i)
    return sum(divisors)


def solution(upper_bound):
    amicable_numbers = []
    for i in range(1, upper_bound):
        b = sum_of_divisors(i)
        if i != b and sum_of_divisors(b) == i:
            if i not in amicable_numbers and i < upper_bound:
                amicable_numbers.append(i)
            if b not in amicable_numbers and b < upper_bound:
                amicable_numbers.append(b)
    return sum(amicable_numbers)


answer = solution(10000)  # Answer evaluates to 31626
