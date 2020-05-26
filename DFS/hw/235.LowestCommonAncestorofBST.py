#235. Lowest Common Ancestor of a Binary Search Tree
"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two 
nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to 
be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]
"""
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Recursion

"""

#-------------------------------------------------------------------------------
#    Soluton1 ---Recursion, D & C
#-------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        parent_val = root.val
        p_val = p.val
        q_val = q.val
        
        # Both at left
        if p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left, p,q)
        # Both at right
        elif p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right, p,q)
        else:
            return root


