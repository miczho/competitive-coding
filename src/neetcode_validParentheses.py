"""
https://neetcode.io/problems/validate-parentheses
https://leetcode.com/problems/valid-parentheses

#blind75 #stack #2024
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        complement = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        stack = []

        for ch in s:
            if ch not in complement:
                stack.append(ch)
            elif stack and stack[-1] == complement[ch]:
                stack.pop()
            else:
                return False

        return len(stack) == 0
