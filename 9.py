import unittest
from numpy import prod

'''
Challenge:

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''


class TestSuite(unittest.TestCase):
    def test_generate_triple(self):
        a, b, c = generate_triple(2, 1)
        assert a == 3 and b == 4 and c == 5

    def test_solution(self):
        assert solution(12) == 60


def generate_triple(m, n):
    # Euclid's formula
    # integers m & n for which m > n > 0
    a = m ** 2 - n ** 2
    b = 2 * m * n
    c = m ** 2 + n ** 2
    return a, b, c


def solution(sum):
    a = 0
    b = 0
    c = 0
    m = 2
    n = 1
    while (a + b + c) != sum:
        a, b, c = generate_triple(m, n)
        m += 1
        n += 1
    return a * b * c


answer = solution(1000)  # FiXME
