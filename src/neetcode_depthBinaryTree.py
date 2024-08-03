"""
DFS solution

https://neetcode.io/problems/depth-of-binary-tree
https://leetcode.com/problems/maximum-depth-of-binary-tree

#blind75 #dfs #2024
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(root == None): return 0

        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)





"""
BFS solution

#bfs
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = 0
        queue = [root]

        while len(queue) != 0:
            nextQueue = []

            for node in queue:
                if node == None:
                    continue
                nextQueue.append(node.left)
                nextQueue.append(node.right)

            result += 1 if len(nextQueue) != 0 else 0
            queue = nextQueue

        return result
