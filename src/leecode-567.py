"""
Time Complexity:
O(n + n + n)
O(n) where n = max(n1, n2)

Space Complexity:
O(n) where n = max(n1, n2)

https://leetcode.com/problems/permutation-in-string/

#2024
"""

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n1 = len(s1)
        n2 = len(s2)

        freq = {}  # O(n) space
        # O(n1) time
        for ch in s1:
            freq[ch] = freq.get(ch, 0) - 1

        # O(n1) time
        for ch in s2[:n1]:
            freq[ch] = freq.get(ch, 0) + 1

            if freq[ch] == 0:
                del freq[ch]

        lo = 0
        hi = n1
        # O(n) time
        while len(freq) != 0 and hi < n2:
            freq[s2[lo]] = freq.get(s2[lo], 0) - 1
            freq[s2[hi]] = freq.get(s2[hi], 0) + 1

            if freq[s2[lo]] == 0:
                del freq[s2[lo]]
            if s2[hi] in freq and freq[s2[hi]] == 0:
                del freq[s2[hi]]
            
            lo += 1
            hi += 1

        return len(freq) == 0
