"""
Can also be solved with DP, but least optimal solution

https://neetcode.io/problems/jump-game-ii
https://leetcode.com/problems/jump-game-ii

#2024 #neetcode150
"""

class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        HEAP SOLUTION

        O(n * log n) time
        O(n) space
        """
        heap = [(0, 0)]

        for i, num in enumerate(nums):
            while heap[0][1] < i:
                heappop(heap)

            heappush(heap, (heap[0][0] + 1, i + num))

        return heap[0][0]


    def jump2(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        GREEDY SOLUTION

        O(n) time
        O(1) space
        """
        n = len(nums)
        maxJump, nextMaxJump = 0, 0
        result = 0

        for i, num in enumerate(nums):
            if i > maxJump:
                maxJump = nextMaxJump
                result += 1

            nextMaxJump = max(nextMaxJump, i + num)

        return result
