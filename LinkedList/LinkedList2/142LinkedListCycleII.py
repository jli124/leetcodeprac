#141. Linked List Cycle
# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
# To represent a cycle in the given linked list, we use an integer pos which represents the position 
#(0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
# Note: Do not modify the linked list.
# #-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Two pointers: fast goes by two steps and slow goes by one step and they meet. One stays at the intersect
and the other start from head, they move in the same speed this time. The second intersect is the entrance of the circle.
"""

#-------------------------------------------------------------------------------
#    Soluton1 - Recursive, O(n) and O(n)
#-------------------------------------------------------------------------------

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersect(self, head):
        slow = fast = head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        
        return None
    
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        
        intersect = self.getIntersect(head)
        if intersect is None:
            return None
        
        ptr1, ptr2 = head, intersect
        
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        return ptr1
    
        