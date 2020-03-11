# 344 Reverse String
"""
Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.
"""
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Recursion

"""

#-------------------------------------------------------------------------------
#    Soluton 
#-------------------------------------------------------------------------------
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if len(s) == 1:
            return s
        
        def swap(l, r):
            if l < r:
                s[l], s[r] = s[r], s[l]
                swap(l + 1, r - 1)
            
        swap(0, len(s) - 1)
            


                         

#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

