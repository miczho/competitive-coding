"""
solved during Weekly Contest 404

https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii

#2024
"""

class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        idx = [-1] * k
        freq = defaultdict(lambda: 0)
        result = 0

        for i in range(n):
            nums[i] %= k

        for i in range(n):
            for j in range(k):
                if idx[nums[i]] <= idx[j]:
                    key = (nums[i], j) if nums[i] > j else (j, nums[i])
                    freq[key] += 1
                    result = max(result, freq[key])
            idx[nums[i]] = i

        return result
