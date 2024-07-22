"""
Time Complexity:
O(N) where N = number of nodes

Space Complexity:
O(N) where N = number of nodes

https://leetcode.com/problems/invert-binary-tree
https://neetcode.io/problems/invert-a-binary-tree

#blind75 #2024
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        queue = [root]

        for node in queue:
            if node == None:
                continue

            tmp = node.left
            node.left = node.right
            node.right = tmp

            queue.append(node.left)
            queue.append(node.right)

        return root
