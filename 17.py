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
            181) == 'OnehundredandEightyOne' and number_to_word(111) == 'OnehundredandEleven'

    def test_solution(self):
        assert solution(5) == 19


def number_to_word(number):
    # Arg number expected as int
    string = ''
    ones_convention = {
        '0': '',
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
        '16': 'Sixteen',
        '17': 'Seventeen',
        '18': 'Eighteen',
        '19': 'Nineteen'
    }
    tens_convention = {
        '0': '',
        '2': 'Twenty',
        '3': 'Thirty',
        '4': 'Forty',
        '5': 'Fifty',
        '6': 'Sixty',
        '7': 'Seventy',
        '8': 'Eighty',
        '9': 'Ninety',
    }

    if number < 20:
        string = ones_convention[str(number)]
    if 19 < number < 100:
        string = tens_convention[str(number)[0]] + ones_convention[str(number)[1]]
    if 99 < number < 1000:
        string = ones_convention[str(number)[0]] + 'hundred'
        if 9 < int(str(number)[1:]) < 20:
            string += 'and' + ones_convention[str(number)[1:]]
        if 0 < int(str(number)[1:]) < 10:  # Prevent key error from looking up 04 as opposed to 4 for example
            string += 'and' + ones_convention[str(number)[2]]
        if int(str(number)[1:]) > 19:
            string += 'and' + tens_convention[str(number)[1]]
            string += ones_convention[str(number)[2]]
    if number == 1000:
        string = 'onethousand'

    return string


def solution(upper_bound):
    # Arg upper_bound expected as int
    result = 0
    for i in range(1, upper_bound + 1):
        result += len(number_to_word(i))
    return result


answer = solution(1000)  # Answer evaluates to 21124
