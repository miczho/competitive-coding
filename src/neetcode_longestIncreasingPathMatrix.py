"""
https://neetcode.io/problems/longest-increasing-path-in-matrix
https://leetcode.com/problems/longest-increasing-path-in-a-matrix

#neetcode150 #2024
"""

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        result = 0
        dp = [[0] * n for _ in range(m)]
        moves = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(x, y):
            if dp[x][y] != 0:
                return dp[x][y]

            maxPath = 1
            for dx, dy in moves:
                xx, yy = x + dx, y + dy
                if 0 <= xx < m and 0 <= yy < n and matrix[xx][yy] > matrix[x][y]:
                    maxPath = max(maxPath, dfs(xx, yy) + 1)
            dp[x][y] = maxPath
            
            return maxPath

        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i, j))

        return result
