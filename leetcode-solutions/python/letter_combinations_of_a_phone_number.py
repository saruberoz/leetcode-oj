# https://oj.leetcode.com/problems/letter-combinations-of-a-phone-number/
#
# Given a digit string, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below.
#
#
#
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
# Although the above answer is in lexicographical order, your answer could be in any order you want.

class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        characters = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxzy'}
        if not digits:
            return ''
        result = ['', '', '']
        for i in range(0, len(digits)):
            if digits[i] not in ('0', '1'):
                result = set([ x + y for x in result for y in characters.get(digits[i])])
        return result


if __name__ == '__main__':
    sol = Solution()
    print sol.letterCombinations('5125')
    print sol.letterCombinations('231')
