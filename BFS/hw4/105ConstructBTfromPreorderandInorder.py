#105. Construct Binary Tree from Preorder and Inorder Traversal
#Given preorder and inorder traversal of a tree, construct the binary tree.
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
DFS
"""

#-------------------------------------------------------------------------------
#    Soluton - O(n)
#-------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder)==0:
            return None
        root=TreeNode(preorder[0])
        middle=inorder.index(preorder[0])
        root.left=self.buildTree(preorder[1:middle+1],inorder[:middle])
        root.right=self.buildTree(preorder[middle+1:],inorder[middle+1:])
        return root



#-------------------------------------------------------------------------------
#    Solution 
#-------------------------------------------------------------------------------
