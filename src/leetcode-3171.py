"""
Was not able to figure it out on my own. Thought of using DP and while it is possible, it is better solved with sliding window.

Time Complexity:
O((n + n) * 32)
= O(32 * 2n)
= O(64n)
= O(n) where n = len(nums)

Space Complexity:
O(32)
= O(1)

https://leetcode.com/problems/find-subarray-with-bitwise-and-closest-to-k/description/

#2024 #favorite #revisit
"""

class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # O(32) space
        self.freqZero = [0] * 32

        INF = float("inf")
        n = len(nums)

        lo, hi = 0, 0
        currK = INF  # start at INF bc the subarr is initially empty
        result = INF

        # O(n + n) time bc 'lo' and 'hi' will both only visit 0 to n-1 once
        while hi != n:
            # expand the window until currK gets too small
            while hi != n and currK > k:
                currK = self.updateAndCalcCurrK(nums[hi], "add")
                result = min(result, abs(currK - k))
                hi += 1

            # shrink the window until currK gets too large
            while lo != hi and currK <= k:
                currK = self.updateAndCalcCurrK(nums[lo], "sub")
                result = min(result, abs(currK - k))
                lo += 1

        return result


    # O(32) time
    def updateAndCalcCurrK(self, val, operater):
        result = 0

        for i in range(32):
            if (val >> i) & 1 == 0:
                if operater == "add":
                    self.freqZero[i] += 1
                elif operater == "sub":
                    self.freqZero[i] -= 1

            if self.freqZero[i] == 0:
                result += 2 ** i

        return result
