"""
Had significant trouble coming up with a solution even though I deduced that DP needed to be used.

DP time complexity formula is:
    Number of DP states * Time it takes to calculate one state

This is bc you only need to calculate every state once,
so the total is the time is takes to calculate all states - #revisit

Time Complexity:
O(N^2 * N)
= O(N^3) where N = length of 's'

Space Complexity:
O(N^2) where N = length of 's'

https://neetcode.io/problems/word-break

#2024
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordDictSet = set(wordDict)
        memo = [[None for _ in range(n + 1)] for _ in range(n + 1)]

        def isWordCombo(start, end):
            if start == end:
                return False
            if s[start:end] in wordDictSet:
                return True

            if memo[start][end] == None:
                memo[start][end] = False
                for middle in range(start, end):
                    if isWordCombo(start, middle) and isWordCombo(middle, end):
                        memo[start][end] = True
                        break

            return memo[start][end]            

        return isWordCombo(0, n)





"""
Attempt 2: Can you reduce the time and space complexity?

Time Complexity:
O(N^2)

Space Complexity:
O(N + M), where N = length of 's' and M = length of 'wordDict'
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDictSet = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] == True and s[j:i] in wordDictSet:
                    dp[i] = True
                    break
        
        return dp[n]


"""
Attempt 3: Can you do the top-down approach with the same time and space complex?

#revisit
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDictSet = set(wordDict)
        n = len(s)
        memo = [None for _ in range(n)]

        def dfs(start):
            if start == n:
                return True

            if memo[start] == None:
                memo[start] = False

                for end in range(start + 1, n + 1):
                    if s[start:end] in wordDictSet and dfs(end):
                        memo[start] = True

            return memo[start]
        
        return dfs(0)
