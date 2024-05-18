"""
https://leetcode.com/problems/unique-paths/

#dp #2024
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        dp = {}  # key: (y-axis, x-axis)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[(i, j)] = 1
                    continue

                dp[(i, j)] = dp.get((i - 1, j), 0) + dp.get((i, j - 1), 0)

        return dp[(m - 1, n - 1)]
