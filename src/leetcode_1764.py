class Solution(object):
    def canChoose(self, groups, nums):
        """
        :type groups: List[List[int]]
        :type nums: List[int]
        :rtype: bool
        """
        m, n = len(groups), len(nums)
        dp = [[-1]*(n+1) for _ in range(m+1)]
        
        def dfs(i, j):
            if i == m:
                return 1
            if j == n:
                return 0
            
            if dp[i][j] == -1:
                ans, skip = 0, False
                for k in range(len(groups[i])):
                    if j+k >= n or groups[i][k] != nums[j+k]:
                        skip = True
                        break
                if not skip:
                    ans |= dfs(i+1, j+len(groups[i]))
                else:
                    ans |= dfs(i, j+1)
                dp[i][j] = ans
            
            return dp[i][j]
        
        
        return dfs(0, 0)