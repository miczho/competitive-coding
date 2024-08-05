"""
https://leetcode.com/problems/repeated-dna-sequences

#2024
"""

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        freq = defaultdict(lambda: 0)
        result = []

        lo, hi = 0, 10
        while hi <= n:
            substr = s[lo:hi]
            freq[substr] += 1
            if freq[substr] == 2:
                result.append(substr)
            lo += 1
            hi += 1

        return result
