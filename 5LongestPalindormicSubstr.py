# 5. Longest Palindromic Substring
"""
Given a string s, find the longest palindromic substring in s. 
You may assume that the maximum length of s is 1000.
"""
#-------------------------------------------------------------------------------
#    Approach- 
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
#    Soluton 1 - List
#-------------------------------------------------------------------------------
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)):
            odd = self.palinAt(s, i, i)
            even = self.palinAt(s, i, i + 1)
            res = max(res, odd, even, key = len)
        return res
        
    def palinAt(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
        
        
#-------------------------------------------------------------------------------
#    test
#-------------------------------------------------------------------------------
