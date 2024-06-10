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
                # case 1: if you select
                newK = k - (1 if prevPos != -1 and nums[prevPos] != nums[currPos] else 0)
                case1 = 1 + dfs(currPos + 1, currPos, newK)
                # case 2: if you don't select
                case2 = dfs(currPos + 1, prevPos, k)

                memo[state] = max(case1, case2)

            return memo[state]


        return dfs(0, -1, k)





"""
Attempt 2:
THIS IS THE EXPECTED SOLUTION

Barely passes (7561ms).
Using an array instead of a dict lowers the time to 6456ms.

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
                    # case 1: 'k' is NOT affected
                    if nums[prevPos] == nums[currPos]:
                        dp[currPos][currK] = max(dp[currPos][currK], dp[prevPos][currK] + 1)
                    # case 2: 'k' is affected
                    elif currK > 0:
                        dp[currPos][currK] = max(dp[currPos][currK], dp[prevPos][currK - 1] + 1)

                result = max(result, dp[currPos][currK])

        return result





"""
Attempt 3:
Inspiration taken from - https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-i/solutions/5280180/java-c-python-dp-o-nk

Instead of saving the index of 'nums' as part of our state, we save the value of 'nums' instead.
The value can be large (10^9), but the length is small (500). We can use a hash map to set our upper bound to the length.
The benefit of using val instead of idx is we can immediately get the longest subsequence ending with a certain val. With idx we would have to loop through to find the our target val.

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
        # is there any way to reduce this to O(1) space???  PROBABLY NOT
        result = defaultdict(lambda: 0)

        # O(n * k) time
        for val in nums:
            # why does looping forwards not work???
            for currK in range(k, -1, -1):
                # max(case 1, case 2)
                dp[val][currK] = max(dp[val][currK] + 1, result[currK - 1] + 1)
                result[currK] = max(result[currK], dp[val][currK])

        # why is the k'th index always the largest value???
        return result[k]





"""
Attempt 4:
F this problem. TLE
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
        # O(n * k) space
        dp = defaultdict(lambda: defaultdict(lambda: 0))
        result = 0

        # O(n * k) time
        for i in range(k + 1):
            # when the previous number is the same as current
            maxSame = defaultdict(lambda: 0)
            # when the previous number is different from current
            maxDiff = 0
            for j in range(n):
                dp[i][j] = max(maxSame[nums[j]] + 1, maxDiff + 1)
                # print("num", nums[j], "k", i, "maxSame", maxSame[nums[j]], "maxDiff", maxDiff, "dp", dp[i][j])

                maxSame[nums[j]] = dp[i][j]
                maxDiff = max(maxDiff, dp[i - 1][j])
                result = max(result, dp[i][j])

        return result
