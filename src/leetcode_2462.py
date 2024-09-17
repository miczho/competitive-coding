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
        loHeap, hiHeap = [], []
        lo, hi = 0, n - 1
        result = 0

        while lo < candidates:
            heappush(loHeap, costs[lo])
            lo += 1

        while hi > n - candidates - 1 and hi >= lo:
            heappush(hiHeap, costs[hi])
            hi -= 1

        for _ in range(k):
            loCost = loHeap[0] if loHeap else INF
            hiCost = hiHeap[0] if hiHeap else INF

            if hiCost < loCost:
                result += hiCost
                heappop(hiHeap)
                if hi >= lo:
                    heappush(hiHeap, costs[hi])
                    hi -= 1
            else:
                result += loCost
                heappop(loHeap)
                if lo <= hi:
                    heappush(loHeap, costs[lo])
                    lo += 1

        return result
