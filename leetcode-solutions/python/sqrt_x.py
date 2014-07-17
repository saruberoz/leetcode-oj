# https://oj.leetcode.com/problems/sqrtx/
# 1016 / 1016 test cases passed.
# Implement int sqrt(int x).
#
# Compute and return the square root of x.


class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x <= 0:
            return 0
        elif x == 1:
            return 1
        l, h = 0, x
        while(h-l > 1):
            mid = l + ((h-l)/2)
            if (mid*mid <= x):
                l = mid
            else:
                h = mid
        return l
