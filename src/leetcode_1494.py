"""
Initial idea was to use topological sort with a heap, popping based on out-degree priority.

However, greedily selecting nodes based on out-degree is incorrect.
Here is a counterexample:
    n = 8
    relations = [[1,3],[1,4],[2,3],[2,4],[5,6],[6,7],[7,8]]
    k = 2

https://leetcode.com/problems/parallel-courses-ii

#2024 #incomplete
"""

class Solution:
    def minNumberOfSemesters(self, n, relations, k):
        """
        :type n: int
        :type relations: List[List[int]]
        :type k: int
        :rtype: int
        """
        nodeChildren = defaultdict(lambda: [])
        inDegree = defaultdict(lambda: 0)
        heap = []
        result = 0
        
        for node, child in relations:
            nodeChildren[node].append(child)
            inDegree[child] += 1

        for node in range(1, n + 1):
            if inDegree[node] == 0:
                outDegree = len(nodeChildren[node])
                heap.append((-outDegree, node))
        heapq.heapify(heap)

        while len(heap) != 0:
            result += 1
            newElements = []

            for _ in range(min(len(heap), k)):
                node = heapq.heappop(heap)[1]

                for child in nodeChildren[node]:
                    inDegree[child] -= 1
                    if inDegree[child] == 0:
                        outDegree = len(nodeChildren[child])
                        newElements.append((-outDegree, child))

            for element in newElements:
                heapq.heappush(heap, element)

        return result
