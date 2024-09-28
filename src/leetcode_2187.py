"""
https://leetcode.com/problems/minimum-time-to-complete-trips/

#2024
"""

class Solution:
    def minimumTime(self, times, totalTrips):
        """
        :type time: List[int]
        :type totalTrips: int
        :rtype: int
        """
        n = len(times)

        def isValid(totalTime):
            return sum(totalTime // time for time in times) >= totalTrips

        lo, hi = 0, totalTrips * min(times)

        while lo + 1 != hi:
            mid = lo + (hi - lo) // 2

            if isValid(mid):
                hi = mid
            else:
                lo = mid

        return hi
