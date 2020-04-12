# 680. Valid Palindrome II
# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
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
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return self.isPalindrome1(s, i+1, j) or self.isPalindrome1(s, i, j-1)
            i += 1
            j -= 1
        return True

    def isPalindrome1(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True



                         

#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

