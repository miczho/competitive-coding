"""
Time Complexity:
O(N) - not 100% sure about this

https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one

#2024
"""

class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [int(ch) for ch in s]
        result = 0

        while len(stack) != 1:
            if stack[-1] == 0:
                stack.pop()
            else:
                cnt = 0
                while len(stack) != 0:
                    ch = stack.pop()
                    if ch == 1:
                        cnt += 1
                    else:
                        break
                stack.append(1)
                for _ in range(cnt):
                    stack.append(0)
            result += 1

        return result
