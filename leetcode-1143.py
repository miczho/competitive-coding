'''
#dp #lcs
'''

import sys

class Solution:
    def longestCommonSubsequence(self, str1: str, str2: str) -> int:
        dp = [[-1] * len(str2) for _ in range(len(str1))]
        

        def LCS(p1, p2):
            if p1 == len(str1) or p2 == len(str2):
                return 0
            
            ans = dp[p1][p2]
            if ans == -1:
                if str1[p1] == str2[p2]:
                    ans = LCS(p1+1, p2+1) + 1
                else:
                    ans = max(LCS(p1+1, p2), LCS(p1, p2+1))
            dp[p1][p2] = ans        
            
            return dp[p1][p2]

        
        return LCS(0, 0)

def main():
    s = Solution()
    print(s.longestCommonSubsequence("abcde", "ace"))

if __name__ == "__main__":
    main()