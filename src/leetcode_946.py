"""
https://leetcode.com/problems/validate-stack-sequences/

#2024
"""


class Solution:
    def validateStackSequences(self, pushed: list, popped: list) -> bool:
        """
        Time complexity:
        O(n)

        Space complexity:
        O(n)
        """

        n = len(pushed)
        stack = []
        p1, p2 = 0, 0

        while p1 != n or p2 != n:
            if stack and stack[-1] == popped[p2]:
                stack.pop()
                p2 += 1
            elif p1 != n:
                stack.append(pushed[p1])
                p1 += 1
            else:
                return False

        return True

    def validateStackSequences2(self, pushed: list, popped: list) -> bool:
        """
        Allocates less space, but modifies the input. Not good practice in a situation like this

        Time complexity:
        O(n)

        Space complexity:
        O(n) modified space
        """

        stackTop = -1
        j = 0

        for num in pushed:
            stackTop += 1
            pushed[stackTop] = num  # Simulates pushing `num` onto the "stack" by placing it at the current stack top

            while stackTop >= 0 and pushed[stackTop] == popped[j]:
                stackTop -= 1
                j += 1

        return stackTop == -1
