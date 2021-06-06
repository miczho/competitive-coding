class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        val = 0
        ans = [0]
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                val += 1
            ans.append(val)

        return sum(ans)