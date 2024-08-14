"""
https://neetcode.io/problems/count-paths
https://leetcode.com/problems/unique-paths

#blind75 #neetcode150 #2024
"""

from collections import defaultdict

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = defaultdict(lambda: 0)

        dp[(0, 0)] = 1

        for i in range(m):
            for j in range(n):
                dp[(i, j)] += dp[(i - 1, j)] + dp[(i, j - 1)]

        return dp[(m - 1, n - 1)]
