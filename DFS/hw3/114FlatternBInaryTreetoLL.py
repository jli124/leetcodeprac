#114. Flatten Binary Tree to Linked List
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Recursion DC

"""

#-------------------------------------------------------------------------------
#    Soluton1 ---D & C
#-------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        ## in place change, no returns
        self.flattenTree(root)
    
    def flattenTree(self, node):
        if not node:
            return None
        
        # there is no child, only the root
        if not node.left and not node.right:
            return node
        
        # divide left and right flat
        left_flat = self.flattenTree(node.left)
        right_flat = self.flattenTree(node.right)
        
        # connect node --> left_flat --> node.right
        if left_flat:
            left_flat.right = node.right
            node.right = node.left
            node.left = None
            
        return right_flat if right_flat else left_flat
#-------------------------------------------------------------------------------
#    Soluton2 - Recursion DFS
#-------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.prev = None
        self.dfs(root)
        
    def dfs(self, root):
        if not root:
        	return None

        self.dfs(root.right)
        self.dfs(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root     