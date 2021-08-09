from collections import defaultdict

class Solution(object):
    def countSpecialSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        freq = defaultdict(int)

        for x in nums:
            if x == 0:
                freq[x] += 1
                freq[x] *= 2
                freq[x] -= 1
            else:
                freq[x] *= 2
                freq[x] += freq[x-1]
            freq[x] %= MOD

        return freq[2]
