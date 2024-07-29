"""
Time Complexity:
O(N*M) where N = length of 'nums1' and M = length of 'nums2'

Space Complexity:
O(N*M) where N = length of 'nums1' and M = length of 'nums2'

https://leetcode.com/problems/max-dot-product-of-two-subsequences

#2024 #favorite #dp
"""

class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
        m = len(nums2)
        dp = {}

        def dfs(i, j):
            if i == n or j == m:
                # returning a large neg number helps to ensure selecting a non-empty subseq
                return float("-inf")

            key = (i, j)

            if key not in dp:
                product = nums1[i] * nums2[j]

                # select nums1[i] and nums2[j] then terminate the search
                case1 = product
                # select nums1[i] and nums2[j] then search for next pair
                case2 = product + dfs(i + 1, j + 1)
                # skip nums1[i]
                case3 = dfs(i + 1, j)
                # skip nums2[j]
                case4 = dfs(i, j + 1)

                dp[key] = max(case1, case2, case3, case4)

            return dp[key]

        return dfs(0, 0)





"""
Attempt 2: iterative approach

#revisit
"""
