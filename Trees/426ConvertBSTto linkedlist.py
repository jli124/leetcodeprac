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
class Solution(object):
    head = None
    prev = None

    def treeToDoublyList(self, root):
        if not root: return None
        self.treeToDoublyListHelper(root)
        self.prev.right = self.head
        self.head.left = self.prev
        return self.head

    def treeToDoublyListHelper(self, node):
        if not node: return
        self.treeToDoublyListHelper(node.left)
        if self.prev:
            node.left = self.prev
            self.prev.right = node
        else:  # We are at the head.
            self.head = node
        self.prev = node
        self.treeToDoublyListHelper(node.right)
                

        