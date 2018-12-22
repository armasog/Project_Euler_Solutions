import unittest
from math import sqrt, ceil

'''
Challenge:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''


class testSuite(unittest.TestCase):
    def test_is_prime(self):
        assert is_prime(7) == True and is_prime(10) == False

    def test_solution(self):
        assert solution(13195) == 29


def is_prime(number):
    for i in range(2, ceil(sqrt(number) + 1)):  # As a property of prime numbers, we only need to test factors less than
        # or equal to the sqrt
        if number % i == 0:
            return False  # If the number is divisible by any number other than itself or 1 is_prime will evaluate to
            #  False and break the loop
    return True


def solution(number):
    prime_factors = []
    nonprime_factorization = number  # Algorithm involves breaking down non_prime factors into their prime factors
    # until only prime factors are left
    for i in range(2, ceil(sqrt(number) + 1)):
        if is_prime(i):
            if nonprime_factorization % i == 0:
                prime_factors.append(i)
                nonprime_factorization = nonprime_factorization / i
    return max(prime_factors)


answer = solution(600851475143)  # Answer evaluates to 6857
