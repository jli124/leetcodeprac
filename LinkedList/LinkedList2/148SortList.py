#148. Sort List
# Sort a linked list in O(n log n) time using constant space complexity.
# #-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
using merge sort
using fast and slow pointer to find the middle point and =None
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
    def merge(self, head1, head2):
        dummy = ListNode(None)
        node = dummy
        while head1 and head2:
            if head1.val < head2.val:
                node.next = head1
                head1 = head1.next
            else:
                node.next = head2
                head2 = head2.next
            node = node.next
            
        node.next = head1 or head2
        return dummy.next 
    
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        # divide into two parts
        slow, fast = head, head.next
        
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            
        second = slow.next
        # cut down the first part
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(second)
        
        return self.merge(l,r)
        
        