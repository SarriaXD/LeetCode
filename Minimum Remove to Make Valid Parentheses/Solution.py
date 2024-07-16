# Given a string s of '(' , ')' and lowercase English characters.
#
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
#
# Formally, a parentheses string is valid if and only if:
#
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
#
#
# Example 1:
#
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# Example 2:
#
# Input: s = "a)b(c)d"
# Output: "ab(c)d"
# Example 3:
#
# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s[i] is either '(' , ')', or lowercase English letter.
# link https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for index, char in enumerate(s):
            if char == '(':
                stack.append((char, index))
            elif char == ')':
                if len(stack) == 0 or stack[-1][0] == ')':
                    stack.append((char, index))
                else:
                    stack.pop()
        if len(stack) == 0:
            return s

        indices_to_remove = [tup[1] for tup in stack]
        indices_set = set(indices_to_remove)
        new_str = ''.join([char for i, char in enumerate(s) if i not in indices_set])
        return new_str


s = Solution().minRemoveToMakeValid("lee(t(c)o)de)")
print(s)


