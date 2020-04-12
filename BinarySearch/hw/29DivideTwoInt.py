#29. Divide Two Integers
"""
Given two integers dividend and divisor, divide two integers without using multiplication, 
division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. 
For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

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
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        isMinus = ((dividend < 0 and divisor > 0) or (dividend > 0 and divisor <0))
        ret, dividend, divisor = 0, abs(dividend), abs(divisor)
        cnt, sub = 1, divisor
        
        while dividend >= divisor:
            if dividend >= sub:
                dividend -= sub
                ret += cnt
                sub = sub << 1 #sub = sub * 2
                cnt = cnt << 1 
            else:
                sub = sub >> 1 #sub = sub / 2
                cnt = cnt >> 1
        if isMinus: ret = -ret
        return min(max(-2147483648,ret),2147483647)
        
#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

