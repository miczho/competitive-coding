"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

https://neetcode.io/problems/meeting-schedule-ii
https://leetcode.com/problems/meeting-rooms-ii

#2024 #blind75 #neetcode150
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
