class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        ans = []
            
        for i in range(n-1, -1, -1):
            m = len(nums[i])
            for j in range(m-1, -1, -1):
                while i + j >= len(ans):
                    ans.append([])
                ans[i+j].append(nums[i][j])
        
        return [item for sublist in ans for item in sublist]