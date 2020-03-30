#102. Binary Tree Level Order Traversal
"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, 
from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
"""
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
bfs
"""

#-------------------------------------------------------------------------------
#    Soluton1 --- BFS 
#-------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    from collections import deque
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        level, levels = 0, []
        queue = collections.deque([root,])
        while queue:
            levels.append([])
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()
                levels[level].append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return levels
#-------------------------------------------------------------------------------
#    Soluton2 ---Recursive
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

