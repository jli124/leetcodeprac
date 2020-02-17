#110. Balanced Binary Tree
#Given a binary tree, determine if it is height-balanced.
#For this problem, a height-balanced binary tree is defined as:
#a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Iterative: root, left, right

"""

#-------------------------------------------------------------------------------
#    Soluton1 ---Iterative
#-------------------------------------------------------------------------------
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        
        paths = []
        stack = [(root,str(root.val))]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                stack.append((node.left, path +'->'+str(node.left.val)))
            if node.right:
                stack.append((node.right, path +'->'+str(node.right.val)))
                
        return paths

#-------------------------------------------------------------------------------
#    Soluton2 ---D & C
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
        return self.isBalancedHelper(root)[0]
    
    def isBalancedHelper(self, root):
        # Empty tree balanced and height -1
        if not root:
            return True, -1

        leftIsBalanced, leftHeight = self.isBalancedHelper(root.left)
        if not leftIsBalanced:
            return False, 0  
        rightIsBalanced, rightHeight = self.isBalancedHelper(root.right)
        if not rightIsBalanced:
            return False, 0
            
        return (abs(leftHeight - rightHeight) <2), 1+ max(leftHeight,rightHeight)
#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

