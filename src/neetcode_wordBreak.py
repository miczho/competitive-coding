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
Attempt 2: Can you lower the time and space complexity?

#revisit
"""
