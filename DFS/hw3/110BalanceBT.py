#110. Balanced Binary Tree
#Given a binary tree, determine if it is height-balanced.
#For this problem, a height-balanced binary tree is defined as:
#a binary tree in which the left and right subtrees of every node differ in height 
#by no more than 1.
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Iterative: root, left, right

"""

#-------------------------------------------------------------------------------
#    Soluton1 ---Iterative
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
#    Soluton2 ---Recursice D & C
#-------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root)[0]
    
    def dfs(self, root):
        # Empty tree balanced and height -1
        if not root:
            return True, -1

        leftIsBalanced, leftHeight = self.dfs(root.left)
        if not leftIsBalanced:
            return False, 0  
        rightIsBalanced, rightHeight = self.dfs(root.right)
        if not rightIsBalanced:
            return False, 0
            
        return (abs(leftHeight - rightHeight) <2), 1+ max(leftHeight,rightHeight)
#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

