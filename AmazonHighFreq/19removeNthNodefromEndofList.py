# 19. Remove Nth Node From End of List
"""
Given a linked list, remove the n-th node from the end of list and return its head.
"""
#-------------------------------------------------------------------------------
#    Approach- 
#-------------------------------------------------------------------------------

#dummy node + two pointer


#-------------------------------------------------------------------------------
#    Soluton 1 - Substring Linear Time Slice O(N/K)
#-------------------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # dummy -> 1 -> 2 ->3 -> 4 -> 5
        
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        
        #first move fast point to n
        for _ in range(n):
            fast = fast.next
        
        # when fast moves to the last position
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # delete the next node of slow
        slow.next = slow.next.next
        return dummy.next


#-------------------------------------------------------------------------------
#    test
#-------------------------------------------------------------------------------
