class Solution(object):
    def getMaximumConsecutive(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        ans = 1
        for c in sorted(coins):
            if c > ans: break
            ans += c
        return ans