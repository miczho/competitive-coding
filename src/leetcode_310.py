"""
https://leetcode.com/problems/minimum-height-trees

#favorite #topSort #2024
"""

class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        children = [set() for _ in range(n)]
        queue = []

        for u, v in edges:
            children[u].add(v)
            children[v].add(u)

        for node in range(n):
            if len(children[node]) <= 1:
                queue.append(node)

        while True:
            nextQueue = []

            for node in queue:
                for child in children[node]:
                    children[child].remove(node)
                    if len(children[child]) == 1:
                        nextQueue.append(child)
                children[node].clear()

            if len(nextQueue) != 0:
                queue = nextQueue
            else:
                break

        return queue
