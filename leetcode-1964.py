from collections import defaultdict

class Solution(object):
    def longestObstacleCourseAtEachPosition(self, obstacles):
        """
        :type obstacles: List[int]
        :rtype: List[int]
        """
        n = len(obstacles)
        d = defaultdict(lambda:float("inf"))
        res = []

        for i, x in enumerate(obstacles):
            lo, hi = 0, i+1
            while hi > lo + 1:
                mid = (lo + hi) // 2
                if d[mid] <= x:
                    lo = mid
                else:
                    hi = mid
            d[lo+1] = min(x, d[lo+1])
            res.append(lo+1)

        return res