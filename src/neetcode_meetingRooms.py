"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

https://neetcode.io/problems/meeting-schedule
https://leetcode.com/problems/meeting-rooms

#2024 #blind75 #neetcode150
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        sortedIntervals = sorted(intervals, key=lambda x: (x.start, x.end))

        for i in range(n - 1):
            end1 = sortedIntervals[i].end
            start2 = sortedIntervals[i + 1].start

            if end1 > start2:
                return False

        return True
