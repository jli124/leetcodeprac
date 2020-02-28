# Implement Queue by Linked List
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Using linked list to implement queue

"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------
class MyQueue:

    def __init__(self):
        ## do intialization if neccessary
    """
    @param: item: An integer
    @return: nothing
    """
        self.dummy =  ListNode(-1)
        self.tail = self.dummy

    def enqueue(self, item):
        node = ListNode(item)
        self.tail.next = node
        self.tail = node

    """
    @return: An integer
    """
    def dequeue(self):
        #record the value before deleting it
        item = self.dummy.next.val
        self.dummy.next = self.dummy.next.next
        # case when delete node is the last node in the linked list. delete the last node
        if self.dummy.next = None:
            self.tail = self.dummy
        retun item

    def empty(self):
        return self.dummy.next is None



        


                         

#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

