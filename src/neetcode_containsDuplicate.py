"""
https://neetcode.io/problems/duplicate-integer
https://leetcode.com/problems/contains-duplicate

#blind75 #neetcode150 #set #hashing #2024
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        past = set()

        for num in nums:
            if num in past:
                return True
            past.add(num)

        return False
