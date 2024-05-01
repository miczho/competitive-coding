"""
Duplicate values ARE allowed. All negatives ARE allowed (you got tripped up by this).

How do I decide if a number is a key or a value? Greedy or DP? Greedy

Time Complexity:
O(n + n * log(n) + n)
= O(n * log(n))
Where n is the length of the array

Space Complexity:
O(n)
Where n is the length of the array

https://leetcode.com/problems/array-of-doubled-pairs/

#2024
"""

class Solution(object):
    def canReorderDoubled(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # O(n) space
        positive = []
        negative = []

        # O(n) time
        for x in arr:
            if x >= 0:
                positive.append(x)
            else:
                negative.append(x)
        
        # O(n * log(n)) time
        positive.sort()
        negative.sort(reverse=True)

        # O(n) time
        return self.canPair(positive) and self.canPair(negative)

    def canPair(self, arr):
        # O(n) space
        freq = {}
        
        for x in arr:
            if x % 2 == 0 and x // 2 in freq:
                freq[x // 2] -= 1
                if freq[x // 2] == 0:
                    del freq[x // 2]
            else:
                if x in freq:
                    freq[x] += 1
                else:
                    freq[x] = 1

        return len(freq) == 0
