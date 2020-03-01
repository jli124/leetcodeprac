#141. Linked List Cycle
# Given a linked list, determine if it has a cycle in it.
# To represent a cycle in the given linked list, we use an integer pos which represents the 
# position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is 
# no cycle in the linked list.
# #-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Two pointers: fast goes by two steps and slow goes by one step, if there is a cycle
they will meet eventually.
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
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow is fast:  # checking whether the two pointers meet
                return True
        
        return False
    
        