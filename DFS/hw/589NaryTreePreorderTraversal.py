# 589. N-ary Tree Preorder Traversal
'''
Given an n-ary tree, return the preorder traversal of its nodes' values.
Nary-Tree input serialization is represented in their level order traversal, 
each group of children is separated by the null value (See examples).
'''
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""


"""

#-------------------------------------------------------------------------------
#    Soluton 1 - Recursion
#-------------------------------------------------------------------------------
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        output = []
        
        def dfs(node):
            if node:
                output.append(node.val)
                for node in (node.children):
                    dfs(node)
            return output
        
        if root:
            dfs(root)
        return output

#-------------------------------------------------------------------------------
#    Soluton 2 -- Iterative
#-------------------------------------------------------------------------------
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
        	return []

        stack, output = [root,], []
        
        while stack:
        	cur = stack.pop()
        	if cur:
        		output.append(cur.val)
        	if cur.children:
        		stack.extend(cur.children[::-1])
        return output                 

#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

