"""
Unable to solve this without looking at solution.

The leetcode equivalent is marked as a favorite.

Time Complexity:
O(N^2)

https://neetcode.io/problems/three-integer-sum

#2024 #blind75
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = set()

        nums.sort()

        for i in range(n):
            j = i + 1
            k = n - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    result.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
        
        return [list(r) for r in result]

if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([-1,0,1,2,-1,-4]))