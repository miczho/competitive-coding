import sys

input = sys.stdin.readline

class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """
        xor = []
        tmp = 0
        for n in nums:
            tmp ^= n
            xor.append(tmp)

        ans = []
        for x in xor:
            ans.append((2 ** maximumBit - 1) ^ x)

        return ans[::-1]


s = Solution()
print(s.getMaximumXor([2,3,4,7], 3))