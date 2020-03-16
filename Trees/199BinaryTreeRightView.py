#199. Binary Tree Right Side View
'''
Given a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.
'''
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
dict: depth:node.val
stack: (node, depth)
"""

#-------------------------------------------------------------------------------
#    Soluton 1 - Recursion
#-------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """            
        rightmost_value_at_depth = dict()
        max_depth = -1
        
        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop()
            
            if node is not None:
                max_depth = max(max_depth, depth)
                rightmost_value_at_depth.setdefault(depth, node.val)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        
        return [rightmost_value_at_depth[depth] for depth in range(max_depth+1)]

        
        



#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

