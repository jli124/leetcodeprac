#69. Sqrt(x)
"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the 
integer part of the result is returned.

"""

#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Binary Search

"""

#-------------------------------------------------------------------------------
#    Soluton1 
#-------------------------------------------------------------------------------
# class TreeNode(object):
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        start, end = 0, x
        while start <= end:
            mid = start  + (end - start) // 2
            if mid **2 == x:
                return mid
            elif mid**2 > x:
                end = mid - 1
            else:
                start = mid + 1
                
        return end
        
#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

