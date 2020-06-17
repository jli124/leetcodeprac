#590. N-ary Tree Postorder Traversal
'''
Given an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, 
each group of children is separated by the null value (See examples).
'''
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Postorder: Left, right, root
Recursion: Method1
Iteration: Method2 (stack)
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
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        self.dfs(root,res)
        return res
    
    def dfs(self, root, res):
            if root:
                res.append(root.val)
                for child in root.children:
                    self.dfs(child,res)
                res.append(root.val) # add the root value last 
           
#-------------------------------------------------------------------------------
#    Soluton 2 -- Iteration O(n)
#-------------------------------------------------------------------------------
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        
        stack, output = [root,], []
        
        while stack:
            curr = stack.pop()
            if curr is not None:
                output.append(curr.val)
            for child in curr.children:
                stack.append(child)
                
        return output[::-1]


#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

