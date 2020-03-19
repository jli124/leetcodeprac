# 705. Design HashSet
"""
Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet. 
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.
"""
#-------------------------------------------------------------------------------
#    Approach- 
#-------------------------------------------------------------------------------

"""
1. Using Linked List 
"""

#-------------------------------------------------------------------------------
#    Soluton 1 - Substring Linear Time Slice O(N/K)
#-------------------------------------------------------------------------------
class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyRange = 769
        self.bucketArray = [Bucket() for i in range(self.keyRange)]
    
    def _hash(self, key):
        return key % self.keyRange

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].insert(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucketIndex = self._hash(key)
        return self.bucketArray[bucketIndex].delete(key)
        
    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        bucketIndex = self._hash(key)
        return self.bucketArray[bucketIndex].exists(key)
        
class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode
        
class Bucket:
    def __init__(self):
        self.head = Node(0)
    
    def insert(self,newValue):
        if not self.exists(newValue):
            newNode = Node(newValue, self.head.next)
            self.head.next = newNode
            
    def delete(self,value):
        prev = self.head
        curr = self.head.next
        while curr is not None:
            if curr.value == value:
                #remove the node
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
        
    def exists(self,value):
        curr = self.head.next
        while curr is not None:
            if curr.value == value:
                return True
            curr = curr.next
        return False      


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

soln = Solution()
#print(soln.strStr(haystack, needle))
#-------------------------------------------------------------------------------
#    test
#-------------------------------------------------------------------------------
