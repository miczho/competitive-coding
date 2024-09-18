"""
https://leetcode.com/problems/subsets
https://neetcode.io/problems/subsets

#2024 #neetcode150
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        stack = []
        result = []

        def dfs(pos=0):
            if pos == n:
                result.append(stack.copy())
            else:
                stack.append(nums[pos])
                dfs(pos + 1)
                stack.pop()
                dfs(pos + 1)

        dfs()

        return result
