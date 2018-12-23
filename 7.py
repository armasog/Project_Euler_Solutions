import unittest
from math import sqrt, ceil

'''
Challenge:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?


'''


class TestSuite(unittest.TestCase):
    def test_is_prime(self):
        assert is_prime(7) and not is_prime(8)

    def test_solution(self):
        assert solution(6) == 13


def is_prime(number):
    for i in range(2, ceil(sqrt(number) + 1)):  # As a property of prime numbers, we only need to test factors less than
        # or equal to the sqrt
        if number % i == 0:
            return False  # If the number is divisible by any number other than itself or 1 is_prime will evaluate to
            #  False and break the loop
    return True


def solution(number):
    prime = 2
    number_of_primes = 0
    i = 1
    while number_of_primes != number:
        if is_prime(i):
            number_of_primes += 1
            prime = i
        i += 1
    return prime


answer = solution(10001)  # Answer evaluates to 104743
