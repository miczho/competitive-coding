import heapq

class Solution(object):
    def getBiggestThree(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])
        distinct = set()
        res = list()
        
        def inBound(x, y):
            return x >= 0 and y >= 0 and x < m and y < n

        def addRes(val):
            if val not in distinct:
                distinct.add(val)
                heapq.heappush(res, -val)
                return True
            return False

        for i in range(m):
            for j in range(n):
                tmp = grid[i][j]
                addRes(tmp)
                l, r, t, b = j-1, j+1, i-1, i+1
                while inBound(i, l) and inBound(i, r) and inBound(t, j) and inBound(b, j):
                    tmp = 0
                    ii, jj = i, l
                    while ii != b or jj != j:
                        tmp += grid[ii][jj]
                        ii += 1; jj += 1
                    while ii != i or jj != r:
                        tmp += grid[ii][jj]
                        ii -= 1; jj += 1
                    while ii != t or jj != j:
                        tmp += grid[ii][jj]
                        ii -= 1; jj -= 1
                    while ii != i or jj != l:
                        tmp += grid[ii][jj]
                        ii += 1; jj -= 1
                    addRes(tmp)
                    l -= 1; r += 1; t -= 1; b += 1

        real_res = list()
        for i in range(min(3, len(res))):
            real_res.append(-heapq.heappop(res))

        return real_res


s = Solution()
print(s.getBiggestThree([[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]))
print(s.getBiggestThree([[20,17,9 ,13,5 ,2 ,9 ,1 ,5 ],
                         [14,9 ,9 ,9 ,16,18,3 ,4 ,12],
                         [18,15,10,20,19,20,15,12,11],
                         [19,16,19,18,8 ,13,15,14,11],
                         [4 ,19,5 ,2 ,19,17,7 ,2 ,2 ]]))  # [107,103,102]