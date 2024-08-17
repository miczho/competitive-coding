"""
Time Complexity:
O(N)

Space Complexity:
O(N)

https://neetcode.io/problems/trapping-rain-water
https://leetcode.com/problems/trapping-rain-water

#blind75 #neetcode150 #dp #2024
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        tallestLeft = [0] * n
        tallestRight = 0
        result = 0

        tallestLeft[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            tallestLeft[i] = max(height[i], tallestLeft[i + 1])

        for i in range(n):
            tallestRight = max(tallestRight, height[i])
            result += min(tallestRight, tallestLeft[i]) - height[i]
        
        return result



"""
Attempt 2: two pointers soln

Time Complexity:
O(N)

Space Complexity:
O(1)

#twoPointers
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        result = 0

        lo, hi = 0, n - 1
        loMax, hiMax = 0, 0
        while lo < hi:
            if height[lo] < height[hi]:
                loMax = max(loMax, height[lo])
                result += loMax - height[lo]
                lo += 1
            else:
                hiMax = max(hiMax, height[hi])
                result += hiMax - height[hi]
                hi -= 1
        
        return result