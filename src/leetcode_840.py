"""
https://leetcode.com/problems/magic-squares-in-grid

#2024
"""

class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        result = 0
        movess = (
            ((0, 0), (0, 1), (0, 2)),
            ((1, 0), (1, 1), (1, 2)),
            ((2, 0), (2, 1), (2, 2)),
            ((0, 0), (1, 0), (2, 0)),
            ((0, 1), (1, 1), (2, 1)),
            ((0, 2), (1, 2), (2, 2)),
            ((0, 0), (1, 1), (2, 2)),
            ((2, 0), (1, 1), (0, 2))
        )

        for i in range(n):
            for j in range(m):
                valid = True
                visited = set()
                for moves in movess:
                    total = 0
                    for move in moves:
                        ii = i + move[0]
                        jj = j + move[1]
                        if 0 <= ii < n and 0 <= jj < m and 0 < grid[ii][jj] < 10:
                            total += grid[ii][jj]
                            visited.add(grid[ii][jj])
                        else:
                            valid = False
                    if total != 15:
                        valid = False
                if len(visited) == 9 and valid:
                    result += 1

        return result
