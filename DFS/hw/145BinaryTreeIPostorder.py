#94. Binary Tree Inorder Traversal
'''
Given a binary tree, return the inorder traversal of its nodes' values.
'''
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Inorder: Right, left, root
Recursion
Iteration:
     the second time visited a node using the algorithm to append stack can acchive binary tree inorder traversal.
"""

#-------------------------------------------------------------------------------
#    Soluton 1 - Iteration 1
#-------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
    
        stack, output = [root,], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)
        
        return output[::-1]

                    
        
#-------------------------------------------------------------------------------
#    Soluton 2 -- Iteration2 O(n)
#-------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        stack, output = [(root,False)], []
        while stack:
            cur, visited = stack.pop()
            if cur:
                if visited:
                    output.append(cur.val)
                else:
                    stack.append((cur, True))
                    stack.append((cur.right,False))
                    stack.append((cur.left,False))
            
        return output


#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

