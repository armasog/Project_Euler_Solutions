import unittest
'''
Challenge:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

'''

class testSuite(unittest.TestCase):
    def test_solution(self):
        assert solution(10) == 23


def solution(upper_bound):
    result = 0
    for i in range(upper_bound):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result

answer = solution(1000)  # Answer is 233168
