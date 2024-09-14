"""
https://neetcode.io/problems/insert-new-interval
https://leetcode.com/problems/insert-interval

#blind75 #neetcode150 #favorite #intervals #2024
"""

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        n = len(intervals)
        result = []

        i = 0
        while i < n:
            start, end = intervals[i]
            newStart, newEnd = newInterval

            # case 1: interval > newInterval -> end loop and append newInterval + remaining greater intervals
            if start > newEnd:
                break
            # case 2: interval < newInterval -> append interval before newInterval
            elif end < newStart:
                result.append(intervals[i])
            # case 3: interval & newInterval overlapping -> merge intervals
            else:
                newInterval = [min(start, newStart), max(end, newEnd)]

            i += 1

        result.append(newInterval)
        result.extend(intervals[i:])

        return result
