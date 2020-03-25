#104. Maximum Depth of Binary Tree
"""
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal,
 each group of children is separated by the null value (See examples).
 """
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Divide and Conquer

"""

#-------------------------------------------------------------------------------
#    Soluton1 ---Iterative
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
#    Soluton2 ---D & C
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
        if root is None:
            return 0
        elif root.children == []:
            return 1
        else:
            child_height = []
            for child in root.children:
                child_height.append(self.maxDepth(child))
        return max(child_height) + 1
        
#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

