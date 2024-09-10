"""
Time Complexity:
O((V + E) log V)

Space Complexity:
O(V + E)

https://leetcode.com/problems/network-delay-time

#2024 #favorite #heap #dijkstra
"""

class Solution:
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        nodeChildren = defaultdict(lambda: [])
        distances = defaultdict(lambda: float("inf"))
        heap = [(0, k)]
        result = 0
        
        for node, child, weight in times:
            nodeChildren[node].append((child, weight))

        distances[k] = 0

        while len(heap) != 0:
            dist, node = heapq.heappop(heap)

            if dist > distances[node]:
                continue

            # At this point, the min dist to 'node' has been finalized
            result = max(result, dist)

            for child, weight in nodeChildren[node]:
                newDist = dist + weight

                if newDist < distances[child]:
                    distances[child] = newDist
                    heapq.heappush(heap, (newDist, child))

        return result if len(distances) == n else -1
