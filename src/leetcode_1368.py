"""
What if you are asked to return shortest distance?
Build a distances lookup table.

What if there are roadblocks?
Check if new cell is blocked.
Need to pass cost into deque to prevent recalculations.

https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/

#favorite #bfs #01bfs #2024
"""

class Solution:
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        INF = float("inf")
        m, n = len(grid), len(grid[0])
        moves = { 1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0) }
        costs = [[INF] * n for _ in range(m)]
        dq = deque([0, 0])

        costs[0][0] = 0

        while dq:
            i, j = dq.pop(), dq.pop()

            if i == m - 1 and j == n - 1:
                break

            for key, move in moves.items():
                iNew, jNew = i + move[0], j + move[1]
                weight = key != grid[i][j]
                newCost = costs[i][j] + weight

                idxOutOfRange = not (0 <= iNew < m and 0 <= jNew < n)
                worseCost = idxOutOfRange or newCost >= costs[iNew][jNew]

                if idxOutOfRange or worseCost:
                    continue

                costs[iNew][jNew] = newCost

                # key part of 0-1 BFS
                if weight == 0:
                    dq.append(jNew)
                    dq.append(iNew)
                else:
                    dq.appendleft(iNew)
                    dq.appendleft(jNew)

        return costs[-1][-1]
