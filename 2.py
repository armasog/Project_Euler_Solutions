import unittest

'''
Challenge: 

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


'''

class testSuite(unittest.TestCase):
    def test_fibonacci_sequence(self):
        assert fibonacci_sequence(10) == [1, 2, 3, 5, 8]

    def test_solution(self):
        assert solution(90) == 44

def fibonacci_sequence(upper_bound):
    result = [1, 2]  # By definition the Fibonacci Sequence begins with the terms 1 and 2
    i = 0
    while i < upper_bound:
        i = result[-1] + result[-2]
        if i < upper_bound:
            result.append(i)
    return result


def solution(upper_bound):
    sequence = fibonacci_sequence(upper_bound)
    result = 0
    for j in sequence:
        if j % 2 == 0:
            result += j
    return result

answer = solution(4000000)  # Answer evaluates to 4613732
