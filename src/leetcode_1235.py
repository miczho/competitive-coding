"""
Time Complexity:
O(NlogN)

Space Complexity:
O(N)

https://leetcode.com/problems/maximum-profit-in-job-scheduling

#interview #2024
"""

class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        n = len(startTime)
        job = []
        dp = {}

        for i in range(n):
            job.append((startTime[i], endTime[i], profit[i]))

        job = sorted(job)

        def dfs(pos):
            if pos == n:
                return 0

            if pos not in dp:
                # case 1: you dont select current job at 'pos'
                # simply go to the next pos

                # case 2: you select current job
                # need to binary search to find the next possible job to select
                lo = pos - 1
                hi = n
                while lo + 1 != hi:
                    mid = lo + (hi - lo) // 2
                    # compare job candidate start time with current job end time
                    if job[mid][0] < job[pos][1]:
                        lo = mid
                    else:
                        hi = mid

                dp[pos] = max(dfs(pos + 1), job[pos][2] + dfs(hi))

            return dp[pos]

        return dfs(0)
