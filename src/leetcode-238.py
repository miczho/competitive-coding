"""
https://leetcode.com/problems/product-of-array-except-self/
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        L, R, answer = [1]*n, [1]*n, [1]*n

        for i in range(1, n):
            L[i] = L[i-1]*nums[i-1]

        for i in reversed(range(0, n-1)):
            R[i] = R[i+1]*nums[i+1]

        for i in range(n):
            answer[i] = L[i]*R[i]
        return answer





"""
Attempt 2

Time Complexity:
O(n + n + n + n)
O(4n)
O(n) where n = length of nums

Space Complexity:
O(n + n + n)
O(3n)
O(n) where n = length of nums

#2024
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        
        front = [1]  # O(n) space
        back = [1]  # O(n) space

        # O(n) time
        for i in range(n):
            front.append(front[-1] * nums[i])

        # O(n) time
        for i in range(n - 1, -1, -1):
            back.append(back[-1] * nums[i])

        back = back[::-1]  # O(n) time

        result = []  # O(n) space

        # O(n) time
        for i in range(n):
            result.append(front[i] * back[i+1])

        return result
