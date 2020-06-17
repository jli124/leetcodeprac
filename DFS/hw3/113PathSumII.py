#113 Path Sum II
"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.
"""
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Iterative 
Recursive

"""

#-------------------------------------------------------------------------------
#    Soluton1 ---Iterative
#-------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        output = []
        stack = [(root, target - root.val, [root.val])]
        while stack:
            node, curr_sum,path = stack.pop()
            if not node.left and not node.right and curr_sum == 0:
                output.append(path)
            if node.left:
                stack.append((node.left, curr_sum - node.left.val, path + [node.left.val]))
            if node.right:
                stack.append((node.right, curr_sum - node.right.val, path + [node.right.val]))

        return output

#-------------------------------------------------------------------------------
#    Soluton2 --- Recursion O(n)
#-------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []

        res = []
        self.dfs(root,target, [], res)
        return res 

    def dfs(self, node, target, path, res):
        if not node.left and not node.right and target == node.val:
            path.append(node.val)
            res.append(path)
        if node.left:
            self.dfs(node.left, target - node.val, path + [node.val], res)
        if node.right:
            self.dfs(node.right, target - node.val, path + [node.val], res)
#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

