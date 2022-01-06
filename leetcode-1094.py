import heapq

class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        trips.sort(key=lambda x:x[1])
        
        h = []
        
        for trip in trips:
            while h and h[0][0] <= trip[1]:
                capacity += h[0][1]
                heapq.heappop(h)
            if capacity >= trip[0]:
                capacity -= trip[0]
                heapq.heappush(h, (trip[2], trip[0]))
            else:
                return False
        
        return True