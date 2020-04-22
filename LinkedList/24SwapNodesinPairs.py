# 24. Swap Nodes in Pairs
"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.
"""

#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""


"""

#-------------------------------------------------------------------------------
#    Soluton1 - Iterative
#-------------------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = prev = ListNode(0)
        dummy.next = head
        
        while head and head.next:
            node1= head
            node2 = head.next
            
            prev.next = node2
            node1.next = node2.next
            node2.next = node1
            # re-initialization
            prev = node1
            head = node1.next
        
        return dummy.next   

#-------------------------------------------------------------------------------
#    Soluton2 - Recursive
#-------------------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if we do not have two nodes to switch
        if not head or not head.next:
            return head

        #set up nodes to swap
        node1 = head
        node2 = head.next
        # swap the two nodes
        node1.next = self.swapPairs(node2.next)
        node2.next = node1

        # return the 2nd node as it is the new head
        return node2

