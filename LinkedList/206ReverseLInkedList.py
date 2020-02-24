# 206. Reverse Linked List
# Reverse a singly linked list.
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Array

"""

#-------------------------------------------------------------------------------
#    Soluton1 - Iterative, O(n) and O(1)
#-------------------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            temp = head.next
            #reverse the direction
            head.next = prev
            # moving the two pointers: prev and head to the same direction
            prev = head
            head = temp
        
        return prev
                         

#-------------------------------------------------------------------------------
#    Soluton2 - Recursive, O(n) and O(n)
#-------------------------------------------------------------------------------
class Solution:
# @param {ListNode} head
# @return {ListNode}
    def reverseList(self, head):
        return self._reverse(head)

    def _reverse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)

