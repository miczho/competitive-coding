"""
solved after Weekly Contest 404

the key to solving the problem is this:
you can find one diameter endpoint of a tree by performing BFS on an arbitrary node
you can find the other diameter endpoint by performing BFS on the first endpoint
here's the proof that this works - https://medium.com/@tbadr/tree-diameter-why-does-two-bfs-solution-work-b17ed71d2881

https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees

#2024 #favorite
"""

class Solution(object):
    def minimumDiameterAfterMerge(self, edges1, edges2):
        """
        :type edges1: List[List[int]]
        :type edges2: List[List[int]]
        :rtype: int
        """
        children1 = [list() for _ in range(len(edges1) + 1)]
        children2 = [list() for _ in range(len(edges2) + 1)]

        for x, y in edges1:
            children1[x].append(y)
            children1[y].append(x)

        for x, y in edges2:
            children2[x].append(y)
            children2[y].append(x)

        pre1 = self.getFarthestNode(0, children1)
        tree1 = self.getFarthestNode(pre1["node"], children1)
        pre2 = self.getFarthestNode(0, children2)
        tree2 = self.getFarthestNode(pre2["node"], children2)

        treeDiameter1 = tree1["length"]
        treeDiameter2 = tree2["length"]
        # +1 added to diameter for ceiling division
        joinedPathLength = ((treeDiameter1 + 1) // 2) + ((treeDiameter2 + 1) // 2) + 1

        return max(treeDiameter1, treeDiameter2, joinedPathLength)

    
    def getFarthestNode(self, start, children):
        farthestNode = start
        length = 0
        visited = set()
        queue = [start]

        while True:
            nextLayer = []

            for node in queue:
                for child in children[node]:
                    if child not in visited:
                        nextLayer.append(child)
                farthestNode = node
                visited.add(node)
            
            if len(nextLayer) != 0:
                queue = nextLayer
                length += 1
            else:
                break

        return { "node": farthestNode, "length": length }
