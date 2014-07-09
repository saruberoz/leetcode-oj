# https://oj.leetcode.com/problems/longest-substring-without-repeating-characters/
# 1002 / 1002 test cases passed.
# Given a string, find the length of the longest substring without repeating characters.
# For example, the longest substring without repeating letters for "abcabcbb" is "abc",
# which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.


class Solution:

    # @return an integer
    def lengthOfLongestSubstring(self, s):
        # use dictionary to contain the unique appeared char
        # {<unique_char>: <index_position>}
        lastRepeatIndex, longestSubstring, results = -1, 0, dict()
        for index in xrange(0, len(s)):
            if s[index] in results and lastRepeatIndex < results[s[index]]:
                lastRepeatIndex = results[s[index]]
            # if we found a longer substring
            # (by diff of index last repeating char and curr index)
            if index - lastRepeatIndex > longestSubstring:
                longestSubstring = index - lastRepeatIndex
            # save the position as value pair
            results [s[index]] = index

        return longestSubstring


if __name__ == '__main__':
    sol = Solution()
    print sol.lengthOfLongestSubstring('') == 0
    print sol.lengthOfLongestSubstring('abcabcbb') == 3
    print sol.lengthOfLongestSubstring('wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco') == 12
    print sol.lengthOfLongestSubstring('hnwnkuewhsqmgbbuqcljjivswmdkqtbxixmvtrrbljptnsnfwzqfjmafadrrwsofsbcnuvqhffbsaqxwpqcac') == 12
