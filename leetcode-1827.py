import sys

input = sys.stdin.readline

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(1, len(nums)):
            if nums[i-1] + 1 > nums[i]:
                ans += nums[i-1] + 1 - nums[i]
                nums[i] += nums[i-1] + 1 - nums[i]

        return ans