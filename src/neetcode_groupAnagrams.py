"""
Asked in TikTok round 2 on 7/22/24

Time Complexity:
O(N*K) where N = number of words and K = number of characters

Space Complexity:
O(N) where N = number of words

https://neetcode.io/problems/anagram-groups
https://leetcode.com/problems/group-anagrams

#blind75 #neetcode150 #2024 #interview
"""

class Solution(object):
    def groupAnagrams(self, words):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = defaultdict(lambda: [])

        for word in words:
            key = [0 for _ in range(26)]
            for ch in word:
                idx = ord(ch) - ord("a")
                key[idx] += 1
            result[tuple(key)].append(word)

        return result.values()
