# 125. Valid Palindrome
# Given a string, determine if it is a palindrome, considering only alphanumeric 
# characters and ignoring cases.
# Note: For the purpose of this problem, we define empty string as valid palindrome.
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
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1
        while l < r:
            # if encounter space from the left -> go to the right char
            while l < r and not s[l].isalnum():
                l += 1
            # if encounter space from the right -> go to the left char
            while l <r and not s[r].isalnum():
                r -= 1
            if (s[l]).lower() != (s[r]).lower():
                return False
            l += 1
            r -= 1
        return True



                         

#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

