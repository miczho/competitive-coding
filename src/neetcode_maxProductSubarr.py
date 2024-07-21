"""
Brute force soln, needs to be solved in O(N).

Time Complexity:
O(N^2)

Space Complexity:
O(1)

https://neetcode.io/problems/maximum-product-subarray

#2024
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        result = float("-inf")

        for i in range(n):
            product = 1
            for j in range(i, n):
                product *= nums[j]
                result = max(result, product)

        return result






"""
Attempt 2: reducing time complexity

Time Complexity:
O(N)

Space Complexity:
O(1)
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
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
