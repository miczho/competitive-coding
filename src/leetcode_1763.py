class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        n, ans = len(s), ""
        for i in range(n):
            freq = {s[i]}
            for j in range(i+1, n):
                freq.add(s[j])
                skip = False
                for k in range(ord('a'), ord('z')+1):
                    if chr(k) in freq:
                        if chr(k).upper() not in freq:
                            skip = True
                            break
                for k in range(ord('A'), ord('Z')+1):
                    if chr(k) in freq:
                        if chr(k).lower() not in freq:
                            skip = True
                            break
                if not skip and j-i+1 > len(ans):
                    ans = s[i:j+1]
        return ans


s = Solution()
print(s.longestNiceSubstring("YazaAay"))