# https://oj.leetcode.com/problems/roman-to-integer/
# Given a roman numeral, convert it to an integer.
#
# Input is guaranteed to be within the range from 1 to 3999.


class Solution:
    # @return an integer
    def romanToInt(self, s):
        roman_number = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                        'C': 100, 'D': 500, 'M': 1000}
        S = list(s)
        res = 0
        for e in s:
            print e, roman_number.get(e)


if __name__ == '__main__':
    sol = Solution()
    sol.romanToInt('XCVII'), 97
