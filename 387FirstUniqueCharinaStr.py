# 387. First Unique Character in a String
"""
Given a string, find the first non-repeating character in it and return it's index. 
If it doesn't exist, return -1.
"""
#-------------------------------------------------------------------------------
#    Approach- 
#-------------------------------------------------------------------------------

"""
stack + string builder (join)
"""

#-------------------------------------------------------------------------------
#    Soluton 1 - Substring Linear Time Slice O(N/K)
#-------------------------------------------------------------------------------
class Solution():
    import collections
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = self.collections.Counter(s)

        for ind, ch in enumerate(s):
            if count[ch] == 1:
                return ind
        return -1



#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------
s = 'loveleetcode'
soln = Solution()
print(soln.firstUniqChar(s))
#-------------------------------------------------------------------------------
#    test
#-------------------------------------------------------------------------------
