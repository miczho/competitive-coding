"""
https://leetcode.com/problems/find-a-safe-walk-through-a-grid

#2024
"""

class Solution:
    def findSafeWalk(self, grid, health):
        """
        :type grid: List[List[int]]
        :type health: int
        :rtype: bool
        """
        m = len(grid)
        n = len(grid[0])
        heap = [(grid[0][0], 0, 0)]
        healthReqs = [[float("inf")] * n for _ in range(m)]
        moves = ((0, 1), (0, -1), (1, 0), (-1, 0))

        healthReqs[0][0] = grid[0][0]

        while heap:
            healthReq, x, y = heappop(heap)

            if x == m - 1 and y == n - 1:
                break
            elif healthReq > healthReqs[x][y]:
                continue

            for xMove, yMove in moves:
                xNew, yNew = x + xMove, y + yMove

                if 0 <= xNew < m and 0 <= yNew < n:
                    newHealthReq = healthReq + grid[xNew][yNew]

                    if newHealthReq < healthReqs[xNew][yNew]:
                        healthReqs[xNew][yNew] = newHealthReq
                        heappush(heap, (newHealthReq, xNew, yNew))

        return healthReqs[-1][-1] < health
