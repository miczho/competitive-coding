"""
Very similar to this problem:
https://leetcode.com/problems/russian-doll-envelopes

https://leetcode.com/problems/length-of-the-longest-increasing-path

#2024
"""

class Solution:
    def maxPathLength(self, coordinates, k):
        """
        :type coordinates: List[List[int]]
        :type k: int
        :rtype: int
        """
        INF = float("inf")
        kCoordinate = coordinates[k]

        # Reverse sorting is important because it prevents counting coordinates with the same 'x' multiple times
        coordinates.sort(key=lambda x: (x[0], -x[1]))

        kNew = coordinates.index(kCoordinate)
        
        def findLongest(arr, xMax=INF, yMax=INF, xMin=-INF, yMin=-INF):
            yArr = []

            for x, y in arr:
                if not (xMin < x < xMax and yMin < y < yMax):
                    continue
                
                pos = bisect_left(yArr, y)

                if pos == len(yArr):
                    yArr.append(y)
                else:
                    yArr[pos] = y

            return len(yArr)

        leftPath = findLongest(coordinates[:kNew], xMax=kCoordinate[0], yMax=kCoordinate[1])
        rightPath = findLongest(coordinates[kNew + 1:], xMin=kCoordinate[0], yMin=kCoordinate[1])

        return 1 + leftPath + rightPath
