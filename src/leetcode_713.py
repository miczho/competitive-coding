"""
Time Complexity:
O(N)

Space Complexity:
O(1)

https://leetcode.com/problems/subarray-product-less-than-k

#2024
"""

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        result = 0
        product = 1

        # hacky workaround to avoid index out of bounds
        nums.append(float("inf"))

        lo, hi = 0, 0
        while hi <= n:
            # this loop is can be merged in to the parent loop
            while product < k and hi <= n:
                result += hi - lo
                product *= nums[hi]
                hi += 1
            
            while product >= k and lo < hi:
                product //= nums[lo]
                lo += 1

            if product >= k:
                hi = n + 1

        return result





"""
Attempt 2: improving readability

#favorite #slidingWindow
"""

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        result = 0
        product = 1

        lo, hi = 0, 0
        while hi < n:
            product *= nums[hi]
            hi += 1
            while product >= k and lo < hi:
                product //= nums[lo]
                lo += 1
            result += hi - lo

        return result
