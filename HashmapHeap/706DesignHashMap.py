# 706. Design HashMap
"""
Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.
"""
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""

"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------
class MyHashMap(object):

    def __init__(self,key=None, value=None):
        """
        Initialize your data structure here.
        """
        self.key = key
        self.value = value
        global hashMap
        hashMap = {}

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        hashMap[key] = value

            
    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        if key in hashMap:
            return hashMap[key]
        else:
            return -1
        
    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        if key in hashMap:
            del hashMap[key]
        else:
            return -1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)


                         

#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

