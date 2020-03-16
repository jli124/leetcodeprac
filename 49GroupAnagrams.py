# 49. Group Anagrams
"""
Given an array of strings, group anagrams together.
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""
#-------------------------------------------------------------------------------
#    Approach- 
#-------------------------------------------------------------------------------

"""
stack 
"""

#-------------------------------------------------------------------------------
#    Soluton1 
#-------------------------------------------------------------------------------
import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)

        return ans.values()
        
                    
        
#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
soln = Solution()
print(soln.groupAnagrams(strs))
