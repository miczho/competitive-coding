"""

https://neetcode.io/problems/longest-repeating-substring-with-replacement
https://leetcode.com/problems/longest-repeating-character-replacement/

#2024 #blind75 #neetcode150 #slidingWindow
"""

class Solution():
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int

        Time complexity:
        O(26n)
        """
        n = len(s)
        freq = defaultdict(lambda: 0)
        result = 0

        lo, hi = 0, 0
        while hi < n:
            freq[s[hi]] += 1
            hi += 1

            while hi - lo - max(freq.values()) > k:
                freq[s[lo]] -= 1

                if freq[s[lo]] == 0:
                    del freq[s[lo]]

                lo += 1

            result = max(result, hi - lo)

        return result


    def characterReplacement2(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int

        Time complexity:
        O(n)
        """
        n = len(s)
        freq, maxFreq = defaultdict(lambda: 0), 0
        result = 0

        lo, hi = 0, 0
        while hi < n:
            freq[s[hi]] += 1
            # 'maxFreq' ONLY needs to be calculated when expanding window size.
            maxFreq = max(maxFreq, freq[s[hi]])
            hi += 1

            while hi - lo - maxFreq > k:
                # 'result' isn't affected when 'maxFreq' decreases, so no need to keep track of such cases
                freq[s[lo]] -= 1
                lo += 1

            result = max(result, hi - lo)

        return result
