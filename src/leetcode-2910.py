"""
After hours of coding and 6 failed submissions, I have concluded that binary search is not a viable approach.
It is NOT TRUE that group size or total groups follows unidirectional True/False pattern.

For example, 
Input: [2, 1, 1, 2, 1, 3, 3, 3, 1, 2, 3, 1, 3, 2, 1, 3, 2, 2, 2]
Frequency: {1: 6, 2: 7, 3: 6}

Next time, it is EXTREMELY IMPORTANT that you prove unidirectional True/False pattern.
Otherwise you go down the wrong path.

https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/

#2024
"""

class Solution(object):
    def minGroupsForValidAssignment(self, balls):
        """
        :type balls: List[int]
        :rtype: int
        """
        self.balls = balls

        # calculate frequency of balls, O(n)
        self.ballFreq = {}
        for ball in balls:
            if ball in self.ballFreq:
                self.ballFreq[ball] += 1
            else:
                self.ballFreq[ball] = 1
        # print("ballFreq", self.ballFreq)

        # binary search, O(log(n))
        result = float('inf')
        lo = 1
        hi = len(balls) + 1
        while hi - lo > 1:
            mid = lo + (hi - lo) // 2
            groups = self.getGroups(mid)

            if groups != float('inf'):
                lo = mid
            else:
                hi = mid

            result = min(result, groups)

        # arr = []
        # for i in range(2, len(balls) + 2):
        #     arr.append(self.getGroups(i))
        # print("arr", arr)

        return result

    # calculate number of groups given group size, O(2n) = O(n)
    def getGroups(self, groupSize):
        result = float("inf")

        # groupSize can be either min val or max val
        groupSizeArr = [
            [groupSize, groupSize + 1],
            [groupSize - 1, groupSize]
        ]
        for minGroupSize, maxGroupSize in groupSizeArr:
            groups = 0
            for freq in self.ballFreq.values():
                if freq % minGroupSize > freq // minGroupSize:
                    groups = float("inf")
                    break
                groups += (freq + maxGroupSize - 1) // maxGroupSize
            result = min(result, groups)

        return result






"""
Attempt 2 with greedy
Time complexity may require a revisit

Time Complexity:
O(n + n + sqrt(n) * 2n)
= O(sqrt(n) * n)
= O(n)
Where n = number of balls

Space Complexity:
O(n)
Where n = number of balls

#revisit
"""

class Solution(object):
    def minGroupsForValidAssignment(self, balls):
        """
        :type balls: List[int]
        :rtype: int
        """
        self.balls = balls

        # calculate frequency of balls, O(n)
        self.ballFreq = {}
        for ball in balls:
            if ball in self.ballFreq:
                self.ballFreq[ball] += 1
            else:
                self.ballFreq[ball] = 1

        # O(n)
        minFreq = float("inf")
        for freq in self.ballFreq.values():
            minFreq = min(minFreq, freq)

        # why is the big O = O(sqrt(n) * n)
        for groupSize in range(max(minFreq, 2), 1, -1):
            result = self.getGroups(groupSize)
            if result != float("inf"):
                return result

        return -1

    # calculate number of groups given group size, O(2n) = O(n)
    def getGroups(self, groupSize):
        result = float("inf")

        # groupSize can be either min val or max val
        groupSizeArr = [
            [groupSize, groupSize + 1],
            [groupSize - 1, groupSize]
        ]
        for minGroupSize, maxGroupSize in groupSizeArr:
            groups = 0
            for freq in self.ballFreq.values():
                if freq % minGroupSize > freq // minGroupSize:
                    groups = float("inf")
                    break
                # number of groups will ALWAYS be ceil(freq / maxGroupSize)
                # https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/solutions/4195877/trivial-clean-python-beats-100-11-lines-proof
                groups += (freq + maxGroupSize - 1) // maxGroupSize
            result = min(result, groups)

        return result