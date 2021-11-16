class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0

        n = len(s)
        letters = set()
        left = 0
        ans = 0

        for right in range(n):
            while s[right] in letters:
                letters.remove(s[left])
                left += 1
            letters.add(s[right])
            ans = max(ans, right - left + 1)

        return ans