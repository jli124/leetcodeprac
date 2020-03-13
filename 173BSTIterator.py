# 173. Binary Search Tree Iterator(M)
"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.
"""
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
stack: last in first out (LIFO)
"""

#-------------------------------------------------------------------------------
#    Soluton1 
#-------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = [] # for the recursion simulation
        self._leftmost_inorder(root)
        

    def _leftmost_inorder(self, root):
        # add all elements in the leftmost branch of the tree for a given node
        while root:
            self.stack.append(root)
            root = root.left
        
    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        topmost_node = self.stack.pop()
        #call the helper func if the node has right child
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        return topmost_node.val
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
#-------------------------------------------------------------------------------
#    Soluton2  - DP
#-------------------------------------------------------------------------------
