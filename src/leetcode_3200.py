"""
solved during Weekly Contest 404

https://leetcode.com/problems/maximum-height-of-a-triangle

#2024
"""

class Solution(object):
    def maxHeightOfTriangle(self, red, blue):
        """
        :type red: int
        :type blue: int
        :rtype: int
        """
        def find(c, red, blue):
            result = 1
            color = c
            while True:
                if color == 'blue':
                    if blue < result:
                        return result - 1
                    blue -= result
                    color = 'red'
                elif color == 'red':
                    if red < result:
                        return result - 1
                    red -= result
                    color = 'blue'
                result += 1
        
        return max(find('blue', red, blue), find('red', red, blue))
