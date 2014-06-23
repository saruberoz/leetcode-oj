# https://oj.leetcode.com/problems/reverse-words-in-a-string/
# 22 / 22 test cases passed.
# Given an input string, reverse the string word by word.
#
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".


class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return ' '.join(s.split()[::-1])
