"""
https://leetcode.com/problems/maximize-score-of-numbers-in-ranges

#2024
"""

class Solution:
    def maxPossibleScore(self, starts: List[int], d: int) -> int:
        n = len(starts)
        sortedStarts = sorted(starts)

        def isValid(space):
            pos = float("-inf")

            for start in sortedStarts:
                if pos + space > start + d:
                    return False
                elif pos + space < start:
                    pos = start
                else:
                    pos += space

            return True

        lo, hi = 0, sortedStarts[-1] + d + 1

        while lo + 1 != hi:
            mid = lo + (hi - lo) // 2

            if isValid(mid):
                lo = mid
            else:
                hi = mid

        return lo
