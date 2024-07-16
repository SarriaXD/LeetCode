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

def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    max_len = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if len(set(s[i:j])) == len(s[i:j]):
                max_len = max(max_len, len(s[i:j]))
            else:
                break
    return max_len