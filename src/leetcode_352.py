"""
https://leetcode.com/problems/data-stream-as-disjoint-intervals/

#2024 #tree #set #map #revisit
"""

class SummaryRanges:
    """
    Solution without using ordered map

    'addNum' time complexity:
    O(n)
    """

    def __init__(self):
        self.intervals = []

    def addNum(self, val: int) -> None:
        new_interval = [val, val]
        merged_intervals = []

        for interval in self.intervals:
            # If the new interval is completely before the current interval
            if new_interval[1] + 1 < interval[0]:
                merged_intervals.append(new_interval)
                new_interval = interval
            # If the new interval is completely after the current interval
            elif interval[1] + 1 < new_interval[0]:
                merged_intervals.append(interval)
            # Overlapping or adjacent intervals, merge them
            else:
                new_interval = [
                    min(new_interval[0], interval[0]),
                    max(new_interval[1], interval[1]),
                ]

        # Add the last interval
        merged_intervals.append(new_interval)
        self.intervals = merged_intervals

    def getIntervals(self) -> list[list[int]]:
        return self.intervals


from sortedcontainers import SortedDict

class SummaryRanges2:
    """
    Using ordered map

    'addNum' time complexity:
    O(logn)
    """

    def __init__(self):
        self.intervals = SortedDict()

    def addNum(self, val: int) -> None:
        if val in self.intervals:
            return

        keys = self.intervals.keys()
        # Find the intervals just before and after `val`
        lower_idx = self.intervals.bisect_left(val) - 1
        upper_idx = self.intervals.bisect_right(val)

        lower_key = keys[lower_idx] if lower_idx >= 0 else None
        upper_key = keys[upper_idx] if upper_idx < len(keys) else None

        start, end = val, val

        # Merge with lower interval if overlapping/adjacent
        if lower_key is not None and self.intervals[lower_key] + 1 >= val:
            start = lower_key
            end = max(end, self.intervals.pop(lower_key))

        # Merge with upper interval if overlapping/adjacent
        if upper_key is not None and upper_key - 1 <= val:
            end = max(end, self.intervals.pop(upper_key))

        # Add the new or merged interval
        self.intervals[start] = end

    def getIntervals(self) -> list[list[int]]:
        return [[k, v] for k, v in self.intervals.items()]


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
