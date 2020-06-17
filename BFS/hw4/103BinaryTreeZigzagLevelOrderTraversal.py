#103. Binary Tree Zigzag Level Order Traversal
"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
return its zigzag level order traversal as:
"""
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
bfs
flag is order_left
deliminitor None after a level is done (Mark for the end of a level and the beginning
of a new level)
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
from collections import deque

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        level_list = []
        if root is None:
            return []
        
        # start with level 0 + delimiter
        queue = deque([root, None])
        is_order_left = True

        while len(queue) > 0:
            curr_node = queue.popleft()

            if curr_node:
                if is_order_left:
                    level_list.append(curr_node.val)
                else:
                    level_list.appendleft(curr_node.val)

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

            else:
                res.append(level_list)
                if len(queue) > 0:
                    queue.append(None)

                #prepare for next level
                level_list = deque()
                is_order_left = not is_order_left

        return res
                
        
#-------------------------------------------------------------------------------
#    Soluton2 ---Recursive
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

