"""
Generic formula for backtracking time complexity = O((Branching Factor)^Depth)
Branching Factor = # of times DFS is called in one layer
Depth = How deep DFS travels

https://neetcode.io/problems/n-queens
https://leetcode.com/problems/n-queens

#neetcode150 #2024
"""

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = []
        col = set()
        total = set()
        diff = set()
        result = []

        def dfs(i):
            if i == n:
                result.append([row for row in board])
                return

            for j in range(n):
                if j not in col and i + j not in total and i - j not in diff:
                    col.add(j)
                    total.add(i + j)
                    diff.add(i - j)
                    board.append("." * j + "Q" + "." * (n - j - 1))

                    dfs(i + 1)
                    
                    col.remove(j)
                    total.remove(i + j)
                    diff.remove(i - j)
                    board.pop()

        dfs(0)
        return result
