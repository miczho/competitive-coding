"""
Time Complexity:
O(N) where N = max(s, t)

Space Complexity:
O(N) where N = max(s, t)

https://leetcode.com/problems/valid-anagram
https://neetcode.io/problems/is-anagram

#blind75 #2024
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        freq = defaultdict(lambda: 0)

        for ch in s:
            freq[ch] += 1
        
        for ch in t:
            freq[ch] -= 1
            if freq[ch] == 0:
                del freq[ch]

        return len(freq) == 0
