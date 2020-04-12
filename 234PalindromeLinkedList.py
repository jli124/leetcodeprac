# 234. Palindrome Linked List
"""
Given a singly linked list, determine if it is a palindrome.
"""
#-------------------------------------------------------------------------------
#    Approach- 
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
#    Soluton 1 - List
#-------------------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        res= []
        curr_node = head
        while curr_node is not None:
            res.append(curr_node.val)
            curr_node = curr_node.next
        return res == res[::-1]
        
#-------------------------------------------------------------------------------
#    test
#-------------------------------------------------------------------------------
