import unittest

'''

Challenge:

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

'''


class TestSuite(unittest.TestCase):
    def test_solution(self):
        assert solution(5) == 3


def solution(upper_bound):
    longest_chain_starting_number = 0
    longest_chain_steps = 0
    previous_sequences = {}  # Keep track of how many steps are in the sequences we've already calculated. Use this
    # information to speed up calculation of future sequences
    for i in range(2, upper_bound):
        current_number = i
        steps = 0
        while current_number != 1:  # 1 signifies the end of the sequence
            if current_number in previous_sequences:
                steps += previous_sequences[current_number]
                break
            else:
                if current_number % 2 == 0:
                    steps += 1
                    current_number = current_number / 2
                else:
                    current_number = (current_number * 3 + 1) / 2
                    steps += 2  # Since an odd number by definition produces an even number next, we can always perform
                    # 2 steps at once
        if steps > longest_chain_steps:
            longest_chain_starting_number = i
            longest_chain_steps = steps
        previous_sequences[i] = steps
    return longest_chain_starting_number


answer = solution(1000000)  # Answer evaluates to 837799
