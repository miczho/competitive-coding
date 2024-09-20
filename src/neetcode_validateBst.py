"""
https://neetcode.io/problems/valid-binary-search-tree
https://leetcode.com/problems/validate-binary-search-tree

#2024 #dfs #blind75 #neetcode150
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        INF = float("inf")

        def dfs(node, minVal=-INF, maxVal=INF):
            if node == None:
                return True

            if not minVal < node.val < maxVal:
                return False

            isLeftValid = dfs(node.left, minVal, node.val)
            isRightValid = dfs(node.right, node.val, maxVal)

            return isLeftValid and isRightValid

        return dfs(root)
