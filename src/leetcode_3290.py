"""
0-1 knapsack, space complexity can be reduced to O(4)

https://leetcode.com/problems/maximum-multiplication-score

#2024
"""

class Solution:
    def maxScore(self, a, b):
        """
        :type a: List[int]
        :type b: List[int]
        :rtype: int
        """
        n, INF = len(b), float("inf")
        dp = [[-INF] * n for _ in range(4)]
        result = -INF

        dp[0][0] = a[0] * b[0]
        for j in range(1, n):
            dp[0][j] = max(dp[0][j - 1], a[0] * b[j])

        for j in range(n):
            for i in range(1, min(j + 1, 4)):
                dp[i][j] = max(
                    dp[i][j - 1],
                    dp[i - 1][j - 1] + a[i] * b[j]
                )
            result = max(result, dp[3][j])

        return result
