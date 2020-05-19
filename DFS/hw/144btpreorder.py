#144. Binary Tree Preoder
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

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        stack,output = [root,],[]
        
        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)
        
        return output

#-------------------------------------------------------------------------------
#    Soluton2 ---Recursive
#-------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(node):
            if not node:
                return
            pre_order.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        pre_order = []
        dfs(root)
        return pre_order
#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

