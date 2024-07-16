# Given a string s, find the length of the longest
# substring
#  without repeating characters.
#
#
#
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
#
# Constraints:
#
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.
# link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        max_len = 0
        i = 0
        j = 1
        s_index = {s[0]: 0}
        while j < len(s):
            current_char = s[j]
            pre_s_index = s_index.get(current_char, -1)
            # current_char is not in the substring
            if pre_s_index < i:
                s_index[current_char] = j
                max_len = max(max_len, j - i + 1)
                j += 1
            else:
                i = pre_s_index + 1

        return max_len
