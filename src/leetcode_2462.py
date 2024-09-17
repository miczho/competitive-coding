"""
https://leetcode.com/problems/total-cost-to-hire-k-workers

#2024
"""

class Solution:
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """
        n, INF = len(costs), float("inf")
        lo, hi = 0, n - 1
        loHeap, hiHeap = [INF], [INF]
        result = 0

        for _ in range(k):
            while len(loHeap) - 1 < candidates and lo <= hi:
                heappush(loHeap, costs[lo])
                lo += 1

            while len(hiHeap) - 1 < candidates and lo <= hi:
                heappush(hiHeap, costs[hi])
                hi -= 1

            if hiHeap[0] < loHeap[0]:
                result += heappop(hiHeap)
            else:
                result += heappop(loHeap)

        return result
