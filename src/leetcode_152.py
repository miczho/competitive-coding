class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.dp = {}

        ans = float('-inf')
        
        self.dfs(0, nums)
        for i in range(len(nums)):
            ans = max(ans, self.dp[(i, 1)])

        return ans

    def dfs(self, pos, nums):
        if pos == len(nums): return (1, 1)

        if (pos, 0) not in self.dp:
            self.dp[(pos, 0)] = min(nums[pos], nums[pos] * self.dfs(pos+1, nums)[0], nums[pos] * self.dfs(pos+1, nums)[1])
            self.dp[(pos, 1)] = max(nums[pos], nums[pos] * self.dfs(pos+1, nums)[0], nums[pos] * self.dfs(pos+1, nums)[1])

        return (self.dp[(pos, 0)], self.dp[(pos, 1)])





"""
Attempt 2: reducing space complexity

Time Complexity:
O(N)

Space Complexity:
O(1)

https://leetcode.com/problems/maximum-product-subarray/
"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currMin = 1
        currMax = 1
        result = float("-inf")

        for num in nums:
            newMin = min(currMin * num, currMax * num, num)
            newMax = max(currMin * num, currMax * num, num)

            currMin = newMin
            currMax = newMax

            result = max(result, currMax)

        return result
