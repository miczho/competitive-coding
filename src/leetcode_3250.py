"""
Time Complexity:
O(N * M)

Space Complexity:
O(M + M)
= O(M)

Where N = length of 'nums' and M = max length of 'nums[i]'

https://leetcode.com/problems/find-the-count-of-monotonic-pairs-i
"""

class Solution(object):
    def countOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        n = len(nums)

        prevNum = nums[0]
        prevDp = defaultdict(lambda: 0)

        # base case: all combinations of first position are valid
        for i in range(prevNum + 1):
            prevDp[i] = i + 1

        for i in range(1, n):
            currNum = nums[i]
            currDp = defaultdict(lambda: 0)

            # make sure to start state computation at first valid seq @ curr position
            for j in range(max(0, currNum - prevNum), currNum + 1):
                # dp & prefix sum
                # current state = max count of valid seq @ prev position + all valid seq @ prev iteration
                currDp[j] = prevDp[min(0, prevNum - currNum) + j] + currDp[j - 1]
                currDp[j] %= MOD

            prevNum = currNum
            prevDp = currDp

        return prevDp[nums[-1]]

