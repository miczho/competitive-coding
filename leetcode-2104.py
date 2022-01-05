class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0
        
        for i in range(n):
            top, bot = nums[i], nums[i]
            for j in range(i+1, n):
                top = max(top, nums[j])
                bot = min(bot, nums[j])
                ans += top - bot
        
        return ans