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
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def construct_paths(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    paths.append(path)
                else:
                    path += '->'
                    construct_paths(root.left, path)
                    construct_paths(root.right, path)
        
        paths = []
        construct_paths(root,'')
        return paths
#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

