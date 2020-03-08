#92. Reverse Linked List II
# Reverse a linked list from position m to n. Do it in one-pass.
# Note: 1 ≤ m ≤ n ≤ length of list.
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""


"""

#-------------------------------------------------------------------------------
#    Soluton - Recursive
#-------------------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = pre = ListNode(0)
        dummy.next = head
        # smaller than m
        for _ in range(m - 1):
            pre = pre.next
        cur = pre.next
        
        # reverse the defined part
        node = None
        for _ in xrange(n - m + 1):
            nxt = cur.next
            cur.next = node
            node = cur
            cur = nxt
            
        # connect the three parts
        pre.next.next = cur
        pre.next = node
        return dummy.next
       
    

#-------------------------------------------------------------------------------
#    Soluton2 
#-------------------------------------------------------------------------------


