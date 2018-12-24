import unittest
from math import ceil, sqrt

'''
Challenge:

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''


class TestSuite(unittest.TestCase):
    def test_is_prime(self):
        assert is_prime(7) and not is_prime(8)

    def test_solution(self):
        assert solution(10) == 17


def is_prime(number):
    for i in range(2, ceil(sqrt(number) + 1)):  # As a property of prime numbers, we only need to test factors less than
        # or equal to the sqrt
        if number == 2:
            return True
        if number % i == 0:
            return False  # If the number is divisible by any number other than itself or 1 is_prime will evaluate to
            #  False and break the loop
    return True


def solution(upper_bound):
    primes = []
    for i in range(2, upper_bound):
        if is_prime(i):
            primes.append(i)
    return sum(primes)


answer = solution(2000000)  # Answer evaluates to 142913828922
