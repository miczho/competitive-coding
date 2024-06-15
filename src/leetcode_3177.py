"""
Solution taken from attempt 3 of 'leetcode-3176.py'

Time Complexity:
O(n * k), where n = length of 'nums'

Space Complexity:
O(n * k + k)
= O(n * k), where n = length of 'nums'

State:
[val][k]

https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-ii/description/
"""

from collections import defaultdict

class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # O(n * k) space
        dp = defaultdict(lambda: defaultdict(lambda: 0))
        # O(k) space
        result = defaultdict(lambda: 0)

        # O(n * k) time
        for val in nums:
            for currK in range(k, -1, -1):
                # max(case 1, case 2)
                dp[val][currK] = max(dp[val][currK] + 1, result[currK - 1] + 1)
                result[currK] = max(result[currK], dp[val][currK])

        return result[k]
