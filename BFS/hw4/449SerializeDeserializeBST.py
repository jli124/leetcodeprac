#449. Serialize and Deserialize BST
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

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preorder(node):
            if node:
                vals.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
        vals = []
        preorder(root)
        return ' '.join(vals)
        
#using 105 construct tree from preorder and inorder traversal
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        preorder = map(int, data.split())
        inorder = sorted(preorder)
        return self.buildTree(preorder, inorder)
    
    def buildTree(self, preorder, inorder):
        if inorder:
            index = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[index])
            root.left = self.buildTree(preorder,inorder[:index])
            root.right = self.buildTree(preorder,inorder[index+1:])
            return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

#-------------------------------------------------------------------------------
#    Solution 
#-------------------------------------------------------------------------------
