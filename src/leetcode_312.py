class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        # dfs
        def findMax(start, end):
            if abs(start - end) == 1:
                return 0
            
            if dp[start][end] == -1:
                for i in range(start+1, end):
                    a = nums[start] * nums[i] * nums[end]
                    b = findMax(start, i)
                    c = findMax(i, end)
                    dp[start][end] = max(dp[start][end], a + b + c)

            return dp[start][end]


        # Main
        nums.insert(0, 1)
        nums.append(1)
        n = len(nums)

        dp = [[-1]*n for i in range(n)]

        return findMax(0, n-1)
