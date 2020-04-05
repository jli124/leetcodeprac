# 58. Length of Last Word
"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', 
return the length of last word (last word means the last appearing word if we loop from left to right) 
in the string.

If the last word does not exist, return 0.
"""
#-------------------------------------------------------------------------------
#    Approach- 
#-------------------------------------------------------------------------------

"""

"""

#-------------------------------------------------------------------------------
#    Soluton 1 
#-------------------------------------------------------------------------------
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        word_list = s.strip().split(' ')
        return len(word_list[-1])

#-------------------------------------------------------------------------------
#    test
#-------------------------------------------------------------------------------
