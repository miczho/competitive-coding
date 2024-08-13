"""
Time Complexity:
O(N*M)

Space Complexity:
O(M)

Where N = length of 's' and M = length of 't'

https://neetcode.io/problems/count-subsequences
https://leetcode.com/problems/distinct-subsequences

#blind75 #neetcode150 #2024
"""

from collections import defaultdict

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n = len(s)
        m = len(t)
        dp = defaultdict(lambda: 0)

        # Base case: There's exactly one way to match an empty t with any prefix of s
        dp[-1] = 1

        # Iterate over each character in s
        for i in range(n):
            # Traverse t in reverse to avoid overwriting the dp values we still need to use in this iteration
            for j in range(m - 1, -1, -1):
                if s[i] == t[j]:
                    # Add the number of ways to form t[:j] to the ways to form t[:j + 1]
                    dp[j] += dp[j - 1]

        return dp[m - 1]
