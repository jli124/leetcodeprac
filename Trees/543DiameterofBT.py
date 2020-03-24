#543. Diameter of Binary Tree
'''
Given a binary tree, you need to compute the length of the diameter of the tree. 
The diameter of a binary tree is the length of the longest path between any two 
nodes in a tree. This path may or may not pass through the root.
'''
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
dfs
"""

#-------------------------------------------------------------------------------
#    Soluton 1 - Recursion
#-------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.dfs(root)
        return self.res
    
    def dfs(self, node):
        if not node:return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.res = max(self.res, left+right) 
        return max(left,right) + 1 


#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

