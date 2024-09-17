"""
https://leetcode.com/problems/longest-increasing-subsequence

#favorite #dp #lis #binarySearch
"""

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        O(n^2) time
        """
        n = len(nums)
        dp = [1] * n
        
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    dp[j] = max(dp[j], dp[i]+1)
        
        return max(dp)
                
                   
    def lengthOfLIS2(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        O(nlogn) time
        """
        n = len(nums)
        tails = []
        
        for val in nums:
            l, r = -1, len(tails)
            
            while l + 1 < r:
                m = l + (r - l) // 2
                if tails[m] >= val:
                    r = m
                else:
                    l = m
            
            if r == len(tails):
                tails.append(val)
            else:
                tails[r] = val
        
        return len(tails)        
