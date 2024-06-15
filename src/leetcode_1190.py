"""
First solution made the wrong assumption that parentheses will have one enclosing.

This example proves that wrong:
Input: "a()(b)"

Time Complexity: O(n^2) (?) where n = length of string
One way to lower the complexity would be to consolidate reverses after the string has been fully parsed.

Space Complexity: O(n) where n = length of string

https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

#2024
"""

from collections import deque

class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        # O(n) space
        self.stack = []

        n = len(s)

        # O(n) time
        for char in s:
            if char == ")":
                # O(n) time
                self.reverse()
            else:
                self.stack.append(char)

        return "".join(self.stack)

    def reverse(self):
        # O(n) space
        queue = deque()

        while len(self.stack) != 0:
            char = self.stack.pop()

            if char == "(":
                break
            
            queue.appendleft(char)
        
        while len(queue) != 0:
            self.stack.append(queue.pop())
