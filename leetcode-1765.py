from collections import deque

class Solution(object):
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(isWater), len(isWater[0])
        vis = [[0]*n for _ in range(m)]
        q = deque()
        ans = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    q.append((i, j))
                    vis[i][j] = 1
        
        imov = (-1, 1, 0, 0)
        jmov = (0, 0, -1, 1)
        
        while q:
            i, j = q.popleft()
            for a in range(4):
                ii, jj = i + imov[a], j + jmov[a]
                if ii < m and ii >= 0:
                    if jj < n and jj >= 0:
                        if vis[ii][jj] == 0:
                            ans[ii][jj] = ans[i][j] + 1
                            q.append((ii, jj))
                            vis[ii][jj] = 1
        
        return ans