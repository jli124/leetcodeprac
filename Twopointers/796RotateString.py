# 796. Rotate String
# We are given two strings, A and B.
# A shift on A consists of taking string A and moving the leftmost character to 
# the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' 
# after one shift on A. Return True if and only if A can become B after some number 
# of shifts on A.
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
two pointers

"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------
class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == B:
            return True

        for i in range(len(A)):
            A = A[1:] + A[0]
            if A == B:
                return True
        return False



                         

#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

