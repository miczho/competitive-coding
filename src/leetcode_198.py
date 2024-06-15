class Solution:
    def rob(self, nums: List[int]) -> int:
        if(len(nums) == 0): return 0
        
        dp = list()
        
        for i in range(len(nums)):
            if len(dp) < 2:
                dp.append(nums[i])
                continue
            
            dp.append(nums[i] + max(dp[:len(dp) - 1]))
            
        return max(dp)