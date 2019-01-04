import unittest

'''
Challenge:

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

'''


class TestSuite(unittest.TestCase):
    def test_solution(self):
        assert solution(2019, 2019) == 52 and solution(2012, 2012) == 53


def solution(startyear, endyear):
    # Accepts args as integers
    '''
    Approach:
    1. Figure out first day of year
        -> Count days from 1 Jan 1901 and use % 7 to figure out
    2. Figure out number of days in year
        -> Figure out if leap year using divisibility rules
    3. Count by 7 to calculate number of Sundays
    '''
    pass
