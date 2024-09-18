"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

Classic 'number of overlapping intervals' problem:
Each start +1 to layers
Each end -1 to layers

https://neetcode.io/problems/meeting-schedule-ii
https://leetcode.com/problems/meeting-rooms-ii

#2024 #blind75 #neetcode150 #intervals
"""

from heapq import heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        sortedIntervals = sorted(intervals, key=lambda x: (x.start, x.end))
        heap = []
        result = 0

        for interval in sortedIntervals:
            while len(heap) != 0 and heap[0] <= interval.start:
                heappop(heap)

            heappush(heap, interval.end)
            result = max(result, len(heap))

        return result


    def minMeetingRooms2(self, intervals: List[Interval]) -> int:
        """
        Each start +1 to layers
        Each end -1 to layers
        """
        parsedIntervals = []
        layers = 0
        result = 0

        for interval in intervals:
            parsedIntervals.append((interval.start, 1))
            parsedIntervals.append((interval.end, -1))

        parsedIntervals.sort()

        for time, val in parsedIntervals:
            layers += val
            result = max(result, layers)

        return result
