"""
Was not able to figure it out on my own. Thought of using DP and while it is possible, it is better solved with sliding window.

The key is to realize that the bitwise OR result can NEVER decrease when you add numbers to the chain.
Similarly, the bitwise OR result can NEVER increase when you remove numbers from the chain.

This requires understanding of how the OR operation works; it only takes one '1' to permanently set the result bit to '1'.

Time Complexity:
O((n + n) * 32)
= O(32 * 2n)
= O(64n)
= O(n) where n = len(nums)

Space Complexity:
O(32)
= O(1)

Note that the O(64n) solution is actually much slower than the O(nlog(n)) solution because log_2(1.8446744e+19) = 64

https://leetcode.com/problems/find-subarray-with-bitwise-or-closest-to-k

#slidingWindow #2024 #favorite #revisit
"""

class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # O(32) space
        self.freqOne = [0] * 32

        INF = float("inf")
        n = len(nums)

        lo, hi = 0, 0
        currK = INF  # start at INF bc the subarr is initially empty
        result = INF

        # O(n + n) time bc 'lo' and 'hi' will both only visit 0 to n-1 once
        while hi != n:
            # expanding the window will always increase currK
            currK = self.updateAndCalcCurrK(nums[hi], "add")
            result = min(result, abs(currK - k))
            hi += 1

            # shrinking the window will always decrease currK
            while lo + 1 != hi and currK > k:
                currK = self.updateAndCalcCurrK(nums[lo], "sub")
                result = min(result, abs(currK - k))
                lo += 1

        return result


    # O(32) time
    def updateAndCalcCurrK(self, val, operater):
        result = 0

        for i in range(32):
            # binary shift the number right and see if the target bit is a '0'
            if (val >> i) & 1 == 1:
                if operater == "add":
                    self.freqOne[i] += 1
                elif operater == "sub":
                    self.freqOne[i] -= 1

            if self.freqOne[i] != 0:
                result += 2 ** i

        return result
