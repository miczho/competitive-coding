"""
First submission TLE, and it took too long to come up with.
Utilizes 3D memoization when it should be done in 2D.

Time Complexity:
O(n^2 * k), where n = length of 'nums'

Space Complexity:
O(n^2 * k), where n = length of 'nums'

State:
[currPos][prevPos][k]

https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-i/

#2024
"""

class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        # O(n^2 * k) space
        memo = {}

        # O(n^2 * k) time
        def dfs(currPos, prevPos, k):
            # previous selection went over limit, so you need to undo
            if k < 0:
                return -1
            elif currPos == n:
                return 0
            
            state = (currPos, prevPos, k)

            if state not in memo:
                # if you select
                newK = k - (1 if prevPos != -1 and nums[prevPos] != nums[currPos] else 0)
                case1 = 1 + dfs(currPos + 1, currPos, newK)
                # if you don't select
                case2 = dfs(currPos + 1, prevPos, k)

                memo[state] = max(case1, case2)

            return memo[state]


        return dfs(0, -1, k)





"""
Attempt 2:
Barely passes (8349ms).
Using an array instead of a dict lowers the time to 6456ms.
Using a string key instead of a tuple is TLE.

Time Complexity:
O(n^2 * k), where n = length of 'nums'

Space Complexity:
O(n * k), where n = length of 'nums'

State:
[currPos][k]

Although the time complexity is theoretically the same, the difference between this
solution passing and not the previous can be mainly attributed to recursive overhead.
"""

from collections import defaultdict

class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        # init all values to 1, where each index is a subsequence
        # O(n * k) space
        dp = defaultdict(lambda: defaultdict(lambda: 1))
        # shortest ans is a single value
        result = 1

        # O(n^2 * k) time
        for currPos in range(n):
            for currK in range(k + 1):
                for prevPos in range(currPos):
                    # 'k' is NOT affected
                    if nums[prevPos] == nums[currPos]:
                        dp[currPos][currK] = max(dp[currPos][currK], dp[prevPos][currK] + 1)
                    # 'k' is affected
                    elif currK > 0:
                        dp[currPos][currK] = max(dp[currPos][currK], dp[prevPos][currK - 1] + 1)

                result = max(result, dp[currPos][currK])

        return result





"""
Attempt 3:
Inspiration taken from - https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-i/solutions/5280180/java-c-python-dp-o-nk

Instead of saving the index of 'nums' as part of our state, we save the value of 'nums' instead.
The value can be large (10^9), but the length is small (500). We can use a hash map to set our upper bound to the length.

We also performed DP on the result. I don't know what's going on anymore.

Time Complexity:
O(n * k), where n = length of 'nums'

Space Complexity:
O(n * k + k)
= O(n * k), where n = length of 'nums'

State:
[val][k]

#revisit
"""

from collections import defaultdict

class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # O(n * k) space
        dp = defaultdict(lambda: defaultdict(lambda: 0))
        # O(k) space
        result = defaultdict(lambda: 0)

        # O(n * k) time
        for val in nums:
            for currK in range(k, -1, -1):
                # 'k' is NOT affected
                # shortened from `dp[val][currK] = max(dp[val][currK], dp[val][currK] + 1)`
                dp[val][currK] += 1
                # 'k' is affected
                if currK > 0:
                    dp[val][currK] = max(dp[val][currK], result[currK - 1] + 1)

                result[currK] = max(result[currK], dp[val][currK])

        return result[k]
