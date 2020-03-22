
# 702. Search in a Sorted Array of Unknown Size
"""
Given an integer array sorted in ascending order, write a function to search target in nums.  I
f target exists, then return its index, otherwise return -1. However, the array size is unknown 
to you. You may only access the array using an ArrayReader interface, where ArrayReader.get(k) 
returns the element of the array at index k (0-indexed).

You may assume all integers in the array are less than 10000, and if you access the array out of bounds, 
ArrayReader.get will return 2147483647.
"""
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Binary search

"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------
class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        # check only one element
        if reader.get(0) == target:
            return 0
        
        
        # define boudaries
        left, right = 0, 1
        while reader.get(right) < target:
            left = right
            # right *= 2 use right shift to speed up
            right <<= 1
        
        # binary search
        while left <= right:
            #mid = (left + right) /2 might cause overflow
            mid = left + ((right-left) >> 1)
            num = reader.get(mid)
            if num == target:
                return mid
            if num > target:
                right = mid -1
            else:
                left = mid + 1
                
        #if no target element
        return -1
        

#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------
n = 5
soln = Solution()
print(soln.firstBadVersion(n))
