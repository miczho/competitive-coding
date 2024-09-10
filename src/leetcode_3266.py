"""
This problem was way above my skill level.

The key is to prove that once `currMinNum * multiplier > originalMaxNum`,
every subsequent iteration results in `currMinNum * multiplier > currMaxNum`.

From there, greedy assign the reset of the iterations.

Time Complexity:
O(NlogK) where N = length of 'nums' and K = 'k'

Space Complexity:
O(N)

https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-ii

#2024
"""

class Solution:
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        if multiplier == 1:
            return nums

        MOD = 10 ** 9 + 7
        n, maxNum = len(nums), max(nums)
        heap = [(num, i) for i, num in enumerate(nums)]
        result = [num for num in nums]

        heapq.heapify(heap)

        while k != 0:
            i = heap[0][1]
            result[i] *= multiplier
            heapq.heapreplace(heap, (result[i], i))
            k -= 1
            # This condition is safisfied quickly
            if result[i] > maxNum:
                break

        kQuotient, kRemainder = divmod(k, n)
        multiMultiplier = pow(multiplier, kQuotient, MOD)

        for _ in range(kRemainder):
            num, i = heapq.heappop(heap)
            result[i] = (num % MOD * multiplier) % MOD

        for i, num in enumerate(result):
            result[i] = (num % MOD * multiMultiplier) % MOD

        return result
