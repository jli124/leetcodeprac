#426. Convert Binary Search Tree to Sorted Doubly Linked List
#Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Iterative: root, left, right

"""

#-------------------------------------------------------------------------------
#    Soluton1 ---D & C
#-------------------------------------------------------------------------------
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def helper(node):
            """
            performs standard inorder traversal:
            left to node to right
            and links all nodes into DLL
            """
            nonlocal last,first
            if node:
                helper(node.left)
                if last:
                    last.right = node
                    node.left = last
                else:
                    first = node
                last = node
                helper(node.right)
                
        if not root:
            return None
        # the smallest and largest nodes
        first, last = None, None
        helper(root)
        last.right = first
        first.left = last
        return first
        