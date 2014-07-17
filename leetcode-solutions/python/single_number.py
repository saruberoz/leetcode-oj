# https://oj.leetcode.com/problems/single-number/
# 15 / 15 test cases passed.
# Given an array of integers, every element appears twice except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        r = 0
        for i in range(0, len(A)):
            r = r ^ A[i]
        return r
