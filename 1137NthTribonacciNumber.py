# 1137. N-th Tribonacci Number
# The Tribonacci sequence Tn is defined as follows: 
#T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
#Given n, return the value of Tn.
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
dynamic programming, list to store the results

"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b, c = 0, 1, 1
        for i in range(n):
            a, b, c = b, c, a + b + c
        return a


                         

#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

