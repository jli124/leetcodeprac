#1290. Convert Binary Number in a Linked List to Integer

# Given head which is a reference node to a singly-linked list. The value of each node 
# in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
# Return the decimal value of the number in the linked list.
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
ans = ans*2 + head
"""

#-------------------------------------------------------------------------------
#    Soluton 
#-------------------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        ans = 0
        while head:
            ans = ans*2 + head.val
            head = head.next
        return ans
        

#-------------------------------------------------------------------------------
#    Soluton2 
#-------------------------------------------------------------------------------


