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
    i = upper_bound - 1
    number_of_successes = 0
    while number_of_successes != upper_bound:
        i += 1
        number_of_successes = 0
        for j in range(1, upper_bound + 1):  # TODO replace with set list to improve performance
            if i % j == 0:  # TODO Shorten list based on shared divisibility rules IE 20 and 2
                number_of_successes += 1
    return i


answer = solution(20)  #
print(answer)
