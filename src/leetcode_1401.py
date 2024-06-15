"""
#geometry
"""

class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        """
        :type radius: int
        :type xCenter: int
        :type yCenter: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        x1 -= xCenter; x2 -= xCenter
        y1 -= yCenter; y2 -= yCenter
        
        xSquared = min(x1**2, x2**2) if x1 * x2 > 0 else 0
        ySquared = min(y1**2, y2**2) if y1 * y2 > 0 else 0
        
        return xSquared + ySquared <= radius ** 2
