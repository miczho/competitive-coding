import sys

input = sys.stdin.readline

class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        for q in queries:
            cnt = 0
            for p in points:
                if ((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2) ** 0.5 <= q[2]:
                    cnt += 1
            ans.append(cnt)

        return ans