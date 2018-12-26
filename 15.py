import unittest
from scipy.special import comb

'''
Challenge:

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

'''


class TestSuite(unittest.TestCase):
    def test_solution(self):
        assert solution(2) == 6


def solution(dimension):
    # Given the geometry of the grid, we know that the number of moves down and moves right must each be equal to the
    # dimension of the grid. To determine the number of possible paths, we need only consider the number of possible
    # moves right using basic combinatronics, since all other moves must then be down.
    return int(comb(2 * dimension, dimension))


answer = solution(20)  # Answer evaluates to 137846528820
