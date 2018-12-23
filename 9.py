import unittest
from math import sqrt

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
        assert solution(25) == 60

# Approach = Write an algorithm to generate Pythagorean triples and test their sums
