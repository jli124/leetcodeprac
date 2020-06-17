#107. Binary Tree Level Order Traversal II
"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

return its bottom-up level order traversal as:
"""
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
bfs
preorder travesal recursion
"""

#-------------------------------------------------------------------------------
#    Soluton1 --- BFS 
#-------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels
        
        def bfs(node, level):
            if len(levels) == level:
                levels.append([])
                
            levels[level].append(node.val)
            
            if node.left:
                bfs(node.left, level + 1)
            
            if node.right:
                bfs(node.right, level + 1)
            
        bfs(root, 0)
        return levels[::-1]
                
        
#-------------------------------------------------------------------------------
#    Soluton2 ---Recursive
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

