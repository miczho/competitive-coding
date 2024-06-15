def find(nums: List[int]) -> int:  
    dp = []

    for i in range(len(nums)):
        if len(dp) < 2:
            dp.append(nums[i])
            continue

        dp.append(nums[i] + max(dp[:len(dp) - 1]))

    return max(dp)

class Solution:
    def rob(self, nums: List[int]) -> int:
        if(len(nums) == 0): return 0
        if(len(nums) == 1): return nums[0]
        
        n = len(nums)

        # How do we prove that the first and last indices are mutually exclusive?
        a = find(nums[:n-1])
        b = find(nums[1:])
        
        return max(a, b)