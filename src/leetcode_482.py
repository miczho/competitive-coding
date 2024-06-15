from collections import deque

class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = s.replace('-', '').upper()
        n = len(s)
        ans = deque()
        
        i = n
        while i > 0:
            ans.appendleft(s[max(0, i-k):i])
            i -= k
        
        return '-'.join(ans)