"""
DP solution

Time Complexity:
O(NlogN)

Space Complexity:
O(N)

https://neetcode.io/problems/non-overlapping-intervals
https://leetcode.com/problems/non-overlapping-intervals

#blind75 #neetcode150 #2024
"""

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        n = len(intervals)
        sortedIntervals = sorted(intervals)
        dp = [-1] * n

        def dfs(pos):
            if pos == n:
                return 0
            if dp[pos] != -1:
                return dp[pos]
            
            lo = pos
            hi = n
            while lo + 1 != hi:
                mid = lo + (hi - lo) // 2
                if sortedIntervals[mid][0] < sortedIntervals[pos][1]:
                    lo = mid
                else:
                    hi = mid
            
            case1 = 1 + dfs(hi)
            case2 = dfs(pos + 1)

            dp[pos] = max(case1, case2)

            return dp[pos]

        return n - dfs(0)





"""
Attempt 2: Greedy solution

Time Complexity:
O(NlogN)

Space Complexity:
O(1)
"""

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        sortedIntervals = sorted(intervals, key=lambda x: x[1])
        curr = float("-inf")
        result = 0

        for start, end in sortedIntervals:
            if start < curr:
                result += 1
            else:
                curr = end
        
        return result
