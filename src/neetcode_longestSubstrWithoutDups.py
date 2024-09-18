"""
https://neetcode.io/problems/longest-substring-without-duplicates
https://leetcode.com/problems/longest-substring-without-repeating-characters

#2024 #blind75 #neetcode150
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        idx = defaultdict(lambda: -1)
        lo = 0
        hi = 0
        result = 0

        while hi < n:
            ch = s[hi]

            if idx[ch] >= lo:
                lo = idx[ch] + 1

            idx[ch] = hi
            hi += 1

            result = max(result, hi - lo)

        return result
