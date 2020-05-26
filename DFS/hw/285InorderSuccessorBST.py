#285. Inorder Successor in BST
'''
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

The successor of a node p is the node with the smallest key greater than p.val.
'''
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Inorder: left -> root -> right
BST: left < root < right
Iteration
"""

#-------------------------------------------------------------------------------
#    Soluton 1 - Iteration
#-------------------------------------------------------------------------------
"""
case 1: Node has right subtree
	go deep to the leftmst node in right subtree /Find min in the right subtree
Case 2: Node has no right subtree
	go to the nearest anscestor for which given node would be in left subtree
"""	
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        # the successor is lower in the right subtree
        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p
    
        # the successor is upper in the tree
        stack, inorder = [], float('-inf')
        while stack or root:
            # go as left as you can
            while root:
                stack.append(root)
                root = root.left
                
            root = stack.pop()
            # if previous node is equal to p, return the current node
            if inorder == p.val:
                return root
            inorder = root.val # update the inorder for each step
            
            #3. go one step to the right
            root = root.right
        
        # if there is no successor
        return None
        """

#-------------------------------------------------------------------------------
#    Soluton 2 
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

