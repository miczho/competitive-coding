# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def dfs(node, depth=0):
            res = (node.val, depth)
            
            if node.left:
                res = dfs(node.left, depth+1)
            if node.right:
                res = max(res, dfs(node.right, depth+1), key=lambda x: x[1])
            
            return res
        
        return dfs(root)[0]
