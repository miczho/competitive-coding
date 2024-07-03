"""
solved during Weekly Contest 404

https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i

#2024
"""

class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even = 0
        odd = 0
        mixed = 0
        mixedTarget = None

        for x in nums:
            if x % 2 == 0:
                even += 1
                if mixedTarget == 'even' or mixedTarget == None:
                    mixedTarget = 'odd'
                    mixed += 1
            else:
                odd += 1
                if mixedTarget == 'odd' or mixedTarget == None:
                    mixedTarget = 'even'
                    mixed += 1
        
        return max(even, odd, mixed)
