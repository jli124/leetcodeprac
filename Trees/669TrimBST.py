#669. Trim a Binary Search Tree
'''
Given a binary search tree and the lowest and highest boundaries as L and R, 
trim the tree so that all its elements lies in [L, R] (R >= L). You might need 
to change the root of the tree, so the result should return the new root of the 
trimmed binary search tree.
'''
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""

Recursion
"""

#-------------------------------------------------------------------------------
#    Soluton 1 
#-------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, tree, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not tree:
            return
        
        tree.left = self.trimBST(tree.left, L, R)
        tree.right = self.trimBST(tree.right, L, R)
        
        if L <= tree.val <= R:
            return tree
        if tree.val < L:
            return tree.right
        if tree.val > R:
            return tree.left
#-------------------------------------------------------------------------------
#    Soluton 2 -- Iterative
#-------------------------------------------------------------------------------
               

#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

