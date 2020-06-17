#236. Lowest Common Ancestor of a Binary Tree
"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node 
in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Recursion

"""

#-------------------------------------------------------------------------------
#    Soluton1 ---Recursion
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
        self.ans = None
        def dfs(node):
            if not node:
                return False
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # if the current node is one of p or q
            mid = node == p or node == q
            if mid + left + right >= 2:
                self.ans = node
                
            return mid or left or right
        
        dfs(root)
        return self.ans


