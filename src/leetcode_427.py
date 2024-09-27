"""
This problem is straight cancer.
Something like this would be used commonly in graphics (e.g. image compression).


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

https://leetcode.com/problems/construct-quad-tree/

#2024
"""

class Solution:
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        n = len(grid)

        def dfs(topLeftCell, bottomRightCell):
            x1, y1 = topLeftCell
            x2, y2 = bottomRightCell

            if topLeftCell == bottomRightCell:
                return Node(grid[x1][y1] == 1, True)

            xSum, ySum = x1 + x2, y1 + y2
            cellPairs = [
                [[x1, y1], [xSum // 2, ySum // 2]],
                [[x1, ySum // 2 + 1], [xSum // 2, y2]],
                [[xSum // 2 + 1, y1], [x2, ySum // 2]],
                [[xSum // 2 + 1, ySum // 2 + 1], [x2, y2]],
            ]
            children = ["topLeft", "topRight", "bottomLeft", "bottomRight"]
            isLeaf = True
            cnt = 0
            result = Node(False, False)

            for cells, child in zip(cellPairs, children):
                setattr(result, child, dfs(*cells))
                isLeaf &= getattr(result, child).isLeaf
                cnt += getattr(result, child).val

            # Node is a leaf if all 4 children are leaves AND have the same val
            if (cnt == 0 or cnt == 4) and isLeaf:
                result.val = cnt == 4
                result.isLeaf = isLeaf
                for child in children:
                    setattr(result, child, None)

            return result

        return dfs([0, 0], [n - 1, n - 1])
