#104. Maximum Depth of Binary Tree
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Iterative

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
        stack,  = [(root,str(root.val))]
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
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.paths = []
        self.dfs(root, '')
        return self.paths
    
    def dfs(self, node, path):
        
        if node:
            path += str(node.val)
            if not node.left and not node.right: 
                self.paths.append(path)  
            else:
                path += '->'  # extend the current path
                self.dfs(node.left, path)
                self.dfs(node.right, path)


