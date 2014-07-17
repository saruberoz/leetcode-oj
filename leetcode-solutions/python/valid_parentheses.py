# https://oj.leetcode.com/problems/valid-parentheses/
# 61 / 61 test cases passed.
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        for e in s:
            if e == '(' or e == '[' or e == '{':
                stack.append(e)
            if e == ')' or e == ']' or e == '}':
                if len(stack) != 0:
                    top = len(stack) - 1
                    if e == ')' and stack[top] == '(':
                        stack.pop()
                    if e == ']' and stack[top] == '[':
                        stack.pop()
                    if e == '}' and stack[top] == '{':
                        stack.pop()
                else:
                    return False
        return len(stack) == 0
