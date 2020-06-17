#559. Maximum Depth of N-ary Tree
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""

"""

#-------------------------------------------------------------------------------
#    Soluton1 ---Recursive
#-------------------------------------------------------------------------------
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        self.maxDepth = 0
        def dfs(root,depth):
            if not root:
                return 
            if not root.children:
                self.maxDepth = max(self.maxDepth, depth)
            if root.children:
                for child in root.children:
                    dfs(child, depth + 1)
        dfs(root, 1)
        return self.maxDepth
        

#-------------------------------------------------------------------------------
#    Soluton2 ---
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

