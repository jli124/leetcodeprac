#104. Maximum Depth of Binary Tree
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Iterative: root, left, right

"""

#-------------------------------------------------------------------------------
#    Soluton1 ---Iterative
#-------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.maxDepth = 0
        def dfs(root, depth):
            if not root:return
            if not root.left and not root.right:
                self.maxDepth = max(self.maxDepth, depth)
            if root.left:dfs(root.left, depth+1)
            if root.right:dfs(root.right, depth+1)
        dfs(root, 1)
        return self.maxDepth

#-------------------------------------------------------------------------------
#    Soluton2 ---D & C
#-------------------------------------------------------------------------------
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height,right_height) + 1
#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

