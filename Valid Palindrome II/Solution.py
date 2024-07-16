# Given a string s, return true if the s can be palindrome after deleting at most one character from it.
#
#
#
# Example 1:
#
# Input: s = "aba"
# Output: true
# Example 2:
#
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:
#
# Input: s = "abc"
# Output: false
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists of lowercase English letters.
# link https://leetcode.com/problems/valid-palindrome-ii/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                if self.validPalindrome_inner(s, i + 1, j) or self.validPalindrome_inner(s, i, j - 1):
                    return True
                else:
                    return False
            i += 1
            j -= 1
        return True

    @staticmethod
    def validPalindrome_inner(s: str, i, j) -> bool:
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

s = "lcuucul"
print(Solution().validPalindrome(s))  # True
