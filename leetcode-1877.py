class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        n = len(nums)
        ans = 0
        for i in range(n // 2):
            ans = max(ans, nums[i] + nums[n - i - 1])

        return ans