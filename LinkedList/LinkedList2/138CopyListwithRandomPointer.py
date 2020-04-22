#138. Copy List with Random Pointer
# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
# Return a deep copy of the list.
# The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.

#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
soln1:
Using hashmap to store old node and new node key, value pair
soln2:
Step 1: Iterate the linked list, create copies of each nodes and insert each copy between its corresponding original node and the next original node (e.g. A-->A'-->B-->B'-->C-->C'-->None)
Step 2: Use the interweaved structure to get the correct reference nodes for random pointers.
Step 3: Take the original and copied linked list
"""

#-------------------------------------------------------------------------------
#    Soluton1 -  O(n) and O(n)
#-------------------------------------------------------------------------------
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution(object):
    def __init__(self):
        #create a dictionary holds old nodes and new nodes as key,value pairs
        self.visitedHash = {}
        
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        if head == None:
            return None
        
        # if we have already processed the current node, then return the cloned version of it.
        if head in self.visitedHash:
            return self.visitedHash[head]
        
        #create a new node with the value same as the old one
        node = Node(head.val, None, None)
        
        #save this value in the hash map
        self.visitedHash[head] = node
        
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        
        return node
#-------------------------------------------------------------------------------
#    Soluton1 - Recursive, O(n) and O(1） space
#-------------------------------------------------------------------------------
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution(object):
    def __init__(self):
        #create a dictionary holds old nodes and new nodes as key,value pairs
        self.visitedHash = {}
        
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        if head == None:
            return None
        self.copyNext(head)
        self.copyRandom(head)
        return self.splitList(head)
    
    def copyNext(self, head):
        curr = head
        while curr:
            cpnode = Node(curr.val, None, None)
            curr.next, cpnode.next = cpnode, curr.next
            curr = curr.next.next
        return curr

    def copyRandom(self, head):
        clone = head
        while clone:
            if clone.random:
                clone.next.random = clone.random.next
            clone = clone.next.next
        return clone

    def splitList(self, head):
        newhead = head.next
        while head:
            temp = head.next
            head.next = temp.next
            head = head.next
            if temp.next:
                temp.next = temp.next.next
        return newhead



        