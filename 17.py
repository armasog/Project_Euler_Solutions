import unittest

'''
Challenge:

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

'''


class TestSuite(unittest.TestCase):
    def test_number_to_word(self):
        assert number_to_word(18) == 'Eighteen' and number_to_word(24) == 'TwentyFour' and number_to_word(
            181) == 'OnehundredandEightyOne'

    def test_solution(self):
        assert solution(5) == 19


def number_to_word(number):
    string = ''  # FIXME handing digits == 0
    if type(number) == list:
        pass  # FIXME handle list output in recursion
    ones_convention = {
        '1': 'One',
        '2': 'Two',
        '3': 'Three',
        '4': 'Four',
        '5': 'Five',
        '6': 'Six',
        '7': 'Seven',
        '8': 'Eight',
        '9': 'Nine',
        '10': 'Ten',
        '11': 'Eleven',
        '12': 'Twelve',
        '13': 'Thirteen',
        '14': 'Fourteen',
        '15': 'Fifteen',
    }
    tens_convention = {
        '2': 'Twenty',
        '3': 'Thirty',
        '4': 'Forty',
        '5': 'Fifty',
        '6': 'Sixty',
        '7': 'Seventy',
        '8': 'Eighty',
        '9': 'Ninety',
    }
    if number > 0 and number <= 15:
        string = ones_convention[str(number)]
    if number == 18:  # Special case to prevent counting as eightteen(sic)
        string = 'Eighteen'
    if number > 15 and number <= 19 and number != 18:
        string = ones_convention[str(number)[1]] + 'teen'
    if number > 19 and number <= 99:
        string = tens_convention[str(number)[0]] + number_to_word(
            [int(str(number)[
                     1])])  # Convert to string to access digit via index and then back to int to use as parameter
    if number > 99:
        string = ones_convention[str(number)[0]] + 'hundredand' + number_to_word(int(
            str(number)[1:]))  # Avoid counting space between hundred and and as per the stipulations of the challenge
    return string


def solution(upper_bound):
    result = 0
    for i in range(1, upper_bound + 1):
        result += len(number_to_word(i))
    return result


answer = solution(1000)
print(answer)
