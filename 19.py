import unittest
'''
Challenge:

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday. (This is incorrect - January 1 1900 was a Tuesday)
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
    def test_is_leap_year(self):
        assert is_leap_year(2012) == True and is_leap_year(2013) == False

    def test_first_day_of_year(self):
        assert first_day_of_year(1910) == 6 and first_day_of_year(2012) == 0
    def test_solution(self):
        assert solution(2019, 2019) == 2 and solution(2012, 2012) == 3


def is_leap_year(year):
    # Accepts arg as integer
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def first_day_of_year(year):
    # Accepts arg as integer >= 1901
    # Returns index corresponding to the day of the week 0 = Sunday, 1 = Monday... 6 = Saturday
    result = 2  # First day of 1901 was a Monday
    days_elapsed = 0  # Since 1/1/1901
    for year in range(1901, year):
        if is_leap_year(year):
            days_elapsed += 366
        else:
            days_elapsed += 365
    days_elapsed += 1  # To get to January 1st of the target year
    result += days_elapsed % 7
    if result > 6:
        result = result % 7
    return result

def solution(startyear, endyear):
    # Accepts args as integers
    number_of_sundays = 0
    for year in range(startyear, endyear + 1):
        first_day = first_day_of_year(year)
        if first_day == 0:
            number_of_sundays += 1
        first_of_month = first_day
        for month in range(1, 12):  # 1 = January, 2 = February, etc.
            if month in [1, 3, 5, 7, 8, 9, 12]:
                first_of_month += (31 % 7)
            else:
                if month == 2:
                    if is_leap_year(year):
                        first_of_month += (29 % 7)
                    else:
                        first_of_month += (28 % 7)
                else:
                    first_of_month += (30 % 7)
            if first_of_month > 6:
                first_of_month = (first_of_month % 6) - 1  # Convert to index corresponding to day of the week
            if first_of_month == 0:
                number_of_sundays += 1
    return number_of_sundays


answer = solution(1901, 2000)  # Answer evaluates to 171
