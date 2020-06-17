#549. Binary Tree Longest Consecutive Sequence II
"""
Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] 
and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid. On the other hand, 
the path can be in the child-Parent-child order, where not necessarily be parent-child order."""
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
DFS
"""

#-------------------------------------------------------------------------------
#    Soluton1 - Recursive
#-------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        self.dfs(root, res)
        return res[0]
    
    def dfs(self, node, res):
        if not node:
            return 0
        
        dcr = inr = 1
        if node.left:
            L = self.dfs(node.left, res)
            if node.val - 1 == node.left.val:
                dcr = L[0] + 1
            elif node.val + 1 == node.left.val:
                inr = L[1] + 1
        if node.right:
            R = self.dfs(node.right, res)
            if node.val - 1 == node.right.val:
                dcr = max(dcr, R[0] + 1)
            elif node.val + 1 == node.right.val:
                inr = max(inr, R[1] + 1)
        res[0] = max(res[0], dcr + inr - 1)
        return [dcr, inr]
                

