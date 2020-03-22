# 1249 Minimum Remove to Make Valid Parentheses
"""
Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
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
class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        ind_to_remove = set()
        stack = []
        for i, c in enumerate(s):
            if c not in "()":
                continue
            if c == '(':
                stack.append(i)
            elif not stack:
                ind_to_remove.add(i)
            ## if it is ")"
            else:
                stack.pop()
        #combine the leftover in stack and ind_to_remove        
        ind_to_remove = ind_to_remove.union(set(stack))
        string_builder = []
        for i, c in enumerate(s):
            if i not in ind_to_remove:
                string_builder.append(c)
        return "".join(string_builder)



#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

soln = Solution()
#print(soln.strStr(haystack, needle))
#-------------------------------------------------------------------------------
#    test
#-------------------------------------------------------------------------------
