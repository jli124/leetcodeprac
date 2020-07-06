# 443. String Compression
"""
Given a string, find the first non-repeating character in it and return its index. 
If it doesn't exist, return -1

"""
#-------------------------------------------------------------------------------
#    Approach- 
#-------------------------------------------------------------------------------

# Two pointer

#-------------------------------------------------------------------------------
#    Soluton  - XOR and hashmap
#-------------------------------------------------------------------------------
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        
        return -1
#-------------------------------------------------------------------------------
#    test
#-------------------------------------------------------------------------------
# soln = Solution()
# print(soln.)