"""
#incomplete
"""

import sys

input = sys.stdin.readline

class Solution(object):
    def makeStringSorted(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        for i in range(1, n+1):
            if s[n-i-1] > s[n-i]:
                # ????