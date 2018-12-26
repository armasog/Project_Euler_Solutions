import unittest

'''
Challenge: 

2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?

'''


class TestSuite(unittest.TestCase):
    def test_solution(self):
        assert solution(2, 15) == 26


def solution(base, exponent):
    result = 0
    value = base ** exponent
    for digit in str(value):  # Convert to string to iterate through each character
        result += int(digit)
    return result


answer = solution(2, 1000)  # Answer evaluates to 1366
