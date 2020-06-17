#298. Binary Tree Longest Consecutive Sequence
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
        L = self.dfs(node.left, res) + 1
        R = self.dfs(node.right, res) + 1
        if node.left is not None and node.val + 1 != node.left.val:
            L = 1
        if node.right is not None and node.val + 1 != node.right.val:
            R = 1
     
        length = max(L, R)
        res[0] = max(res[0], length)
        return length
#-------------------------------------------------------------------------------
#    Solution2 - Iterative
#-------------------------------------------------------------------------------
class Solution(object):
    
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0

        stack = [(root, 1)]
        res = 0

        while stack:
            node, length = stack.pop()
            if node.left:
                stack.append((node.left, length + 1 if node.left.val == node.val + 1 else 1))
            if node.right:
                stack.append((node.right, length + 1 if node.right.val = node.val + 1 else 1))

            res = max(res, length)
        return res


