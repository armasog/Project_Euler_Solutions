from math import sqrt
import unittest

'''
Challenge:

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

class TestSuite(unittest.TestCase):
    def test_solution(self):
        assert solution(12) == 60.0


def quadratic_formula(c, sum):
    # We start with two equations: a + b + c = sum and a**2 + b**2 = c**2
    # Using substitution we can rearrange a**2 + b**2 into a quadratic equation
    # We can thus use the quadratic equation to find possible values for a using a given c value
    a1 = -(-2 * sum + 2 * c) + sqrt((-2 * sum + 2 * c) ** 2 - 4 * 2 * (sum ** 2 - 2 * sum * c))
    a1 = a1 / 4
    a2 = -(-2 * sum + 2 * c) - sqrt((-2 * sum + 2 * c) ** 2 - 4 * 2 * (sum ** 2 - 2 * sum * c))
    a2 = a2 / 4
    return a1, a2


def find_b(a, c):
    # Rearrange the equation a**2 + b**2 = c**2
    return sqrt(c ** 2 - a ** 2)


def solution(sum):
    for c in range(1, 999999999):
        b = 0
        try:
            result1, result2 = quadratic_formula(c, sum)
            if result1.is_integer() and result1 >= 0:  # Pythagorean triples can only consist of positive integers
                b = find_b(result1, c)
                if result1 + b + c == sum:
                    break
            if result2.is_integer() and result2 >= 0:
                b = find_b(result2, c)
                if result1 + b + c == sum:
                    break
        except ValueError:  # Catches domain error when trying to take the sqrt of a negative number as part of the
            # quadratic formula
            continue
    return result1 * b * c


answer = solution(1000)  # Answer evaluates to 31875000.0
