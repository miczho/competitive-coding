"""
https://neetcode.io/problems/merge-intervals
https://leetcode.com/problems/merge-intervals

#2024 #blind75 #neetcode150
"""

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(intervals)
        sortedIntervals = sorted(intervals)
        result = [sortedIntervals[0]]

        for i in range(1, n):
            start1, end1 = sortedIntervals[i]
            end2 = result[-1][1]

            # Checking end1 >= start2 not needed, handled by sorting
            # Sorting guarantees start1 <= start2
            if start1 <= end2:
                result[-1][1] = max(end1, end2)
            else:
                result.append(sortedIntervals[i])

        return result