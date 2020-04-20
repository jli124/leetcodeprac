#25. Reverse Nodes in k-Group
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# k is a positive integer and is less than or equal to the length of the linked list. 
# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Use a dummy head, and

l, r : define reversing range

pre, cur : used in reversing, standard reverse linked linked list method

jump : used to connect last node in previous k-group to first node in following k-group

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
    def reverseKGroup(self, head, k):
        dummy = jump = ListNode(0)
        dummy.next = l = r = head

        while True:
            count = 0
            # use r to locate the range
            while r and count < k:
                r = r.next
                count += 1
            if count == k:
                pre, cur = r, l
                for _ in range(k):
                    # standard reversing
                    cur.next, cur, pre = pre, cur.next, cur 
                # connect two groups
                jump.next, jump, l = pre, l, r
            else:
                return dummy.next


#-------------------------------------------------------------------------------
#    Soluton2 - Recursive, O(n) and O(n)
#-------------------------------------------------------------------------------
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        count = 0
        prev = head
        while count < k and prev:
            prev = prev.next
            count += 1
        if count == k:
            rev_head = self.reverseLinkedList(head,k)
            head.next = self.reverseKGroup(prev, k)  
            return rev_head
        return head
    
    def reverseLinkedList(self, head, k):
        curr, prev = None, head
        
        while k:
            temp = prev.next
            prev.next = curr
            curr = prev
            prev = temp
            k -= 1
        return curr
    
    

