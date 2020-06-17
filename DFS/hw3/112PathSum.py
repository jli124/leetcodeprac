#112 Path Sum
"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path 
such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.
"""
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
https://leetcode.com/problems/path-sum/discuss/36486/Python-solutions-
(DFS-recursively-DFS%2Bstack-BFS%2Bqueue)

"""

#-------------------------------------------------------------------------------
#    Soluton1 ---Iterative (DFS)
#-------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        
        
        stack = [(root, target - root.val)]
        while stack:
            node, curr_sum = stack.pop()
            if not node.left and not node.right and curr_sum == 0:
                return True
            if node.right:
                stack.append((node.right, curr_sum - node.right.val))
            if node.left:
                stack.append((node.left, curr_sum - node.left.val))
                
        return False
#-------------------------------------------------------------------------------
#    Soluton2 ---Iterative (BFS + queue)
#-------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        
        
        queue = [(root, target - root.val)]
        while queue:
            node, curr_sum = queue.pop(0)
            if not node.left and not node.right and curr_sum == 0:
                return True
            if node.left:
                queue.append((node.left, curr_sum - node.left.val))
            if node.right:
                queue.append((node.right, curr_sum - node.right.val))
                
        return False
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
    def hasPathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        res = [False]
        self.dfs(root, target, res)
        return res[0]
        
    def dfs(self, node, target_sum, res):
        if node:
            if not node.left and  not node.right:
                if node.val == target_sum: res[0] = True
            if node.left:
                self.dfs(node.left, target_sum - node.val, res)
            if node.right:
                self.dfs(node.right, target_sum - node.val, res)            

            
        # target -= root.val
        # if not root.left and not root.right:
        #     return target == 0
        # return self.hasPathSum(root.left, target) or self.hasPathSum(root.right, target)
            
#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

