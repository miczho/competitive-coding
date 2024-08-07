"""
Assuming M = length of 'houses' and N = length of 'heaters'

Time Complexity:
O(NlogN + MlogN)

Space Complexity:
O(1)

https://leetcode.com/problems/heaters

#favorite #binarySearch #2024
"""

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        n = len(heaters)
        result = 0

        heaters.sort()

        for house in houses:
            lo, hi = 0, n - 1
            while lo + 1 < hi:
                mid = lo + (hi - lo) // 2
                if heaters[mid] < house:
                    lo = mid
                else:
                    hi = mid

            dist1 = abs(house - heaters[lo])
            dist2 = abs(house - heaters[hi])

            result = max(result, min(dist1, dist2))

        return result





"""
Attempt 2: two pointers soln

Assuming M = length of 'houses' and N = length of 'heaters'

Time Complexity:
O(MlogM + NlogN + M + N)

Space Complexity:
O(1)

#twoPointers
"""

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        n = len(heaters)
        result = 0

        houses.sort()
        heaters.sort()

        i = 0
        for house in houses:
            while i < n - 1 and heaters[i] + heaters[i + 1] <= house * 2:
                i += 1
            result = max(result, abs(heaters[i] - house))

        return result
