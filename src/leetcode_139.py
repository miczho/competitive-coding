"""
https://leetcode.com/problems/word-break
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
