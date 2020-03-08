#160. Intersection of Two Linked Lists
# Write a program to find the node at which the intersection of two singly linked lists begins.
# For example, the following two linked lists
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Two pointer starting from A and B separately
Switch head when either pointer hits the end to account fo the possible difference
"""

#-------------------------------------------------------------------------------
#    Soluton - Two pointer
#-------------------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        ptr_a = headA
        ptr_b = headB
        
        while ptr_a is not ptr_b:
            if ptr_a:
                ptr_a = ptr_a.next
            else:
                ptr_a = headB
            if ptr_b:
                ptr_b = ptr_b.next
            else:
                ptr_b = headA
        return ptr_a
    

#-------------------------------------------------------------------------------
#    Soluton2 
#-------------------------------------------------------------------------------


