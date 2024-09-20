"""
https://leetcode.com/problems/reach-end-of-array-with-max-score

#2024
"""

class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        maxNum = 0
        result = 0

        for num in nums:
            result += maxNum
            maxNum = max(maxNum, num)

        return result
