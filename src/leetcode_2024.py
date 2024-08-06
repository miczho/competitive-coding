"""
https://leetcode.com/problems/maximize-the-confusion-of-an-exam

#2024
"""

class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        n = len(answerKey)
        freq = defaultdict(lambda: 0)
        result = 0

        lo, hi = 0, 0
        while hi < n:
            freq[answerKey[hi]] += 1
            hi += 1
            while freq["T"] > k and freq["F"] > k:
                freq[answerKey[lo]] -= 1
                lo += 1
            result = max(result, hi - lo)

        return result
