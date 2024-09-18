"""
DP solution is O(n^2) time

https://leetcode.com/problems/longest-increasing-subsequence
https://neetcode.io/problems/longest-increasing-subsequence

#2024 #blind75 #neetcod150 #favorite #lis #binarySearch
"""

from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Time complexity:
        O(n * log n)
        """
        sequence = []

        for num in nums:
            i = bisect_left(sequence, num)

            if i == len(sequence):
                sequence.append(num)
            else:
                sequence[i] = num

        return len(sequence)
