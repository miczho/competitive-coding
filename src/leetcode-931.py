"""
#dp #hashMap
"""

import sys

class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n, dp = len(matrix), {}
        def dfs(x, y):
            if x == -1:
                return 0

            if (x, y) not in dp:
                res = dfs(x-1, y)
                if y-1 >= 0:
                    res = min(res, dfs(x-1, y-1))
                if y+1 < n:
                    res = min(res, dfs(x-1, y+1))
                dp[(x, y)] = matrix[x][y] + res

            return dp[(x, y)]

        ans = dfs(n-1, 0)
        for i in range(1, n):
            ans = min(ans, dfs(n-1, i))

        return ans
        


def main():
    s = Solution()
    print(s.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))
    print(s.minFallingPathSum([[-19,57],[-40,-5]]))
    print(s.minFallingPathSum([[-48]]))


if __name__ == '__main__':
    main()