#1120. Maximum Average Subtree
#Given the root of a binary tree, find the maximum average value of any subtree of that tree.
#(A subtree of a tree is any node of that tree plus all its descendants. The average value of 
#a tree is the sum of its values, divided by the number of nodes.)
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Iterative: root, left, right

"""

#-------------------------------------------------------------------------------
#    Soluton1 ---D & C
#-------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maximumAverageSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: float
        """
        self.res = 0
        def helper(root):
            if not root:
                return [0, 0.0]
            n_left, sum_left = helper(root.left)
            n_right, sum_right = helper(root.right)
            n_total = n_left + n_right + 1
            sum_total = sum_left + sum_right + root.val
            self.res = max(self.res, sum_total/n_total)
            return [n_total, sum_total]
            
        helper(root)
        return self.res

