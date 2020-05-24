#94. Binary Tree Inorder Traversal
'''
Given a binary tree, return the inorder traversal of its nodes' values.
'''
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Inorder: Left, root, right
Recursion
Iteration:
     the second time visited a node using the algorithm to append stack can acchive binary tree inorder traversal.
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
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.inorder_helper(root,res)
        return res
    
        # inorder: left, root, right
    def inorder_helper(self,node,res):
        if node:
            self.inorder_helper(node.left,res)
            res.append(node.val)
            self.inorder_helper(node.right,res)
        

                    
        
#-------------------------------------------------------------------------------
#    Soluton 2 -- Iteration O(n)
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
                    stack.append((cur.right,False))
                    stack.append((cur, True))
                    stack.append((cur.left,False))
            
        return output


#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

