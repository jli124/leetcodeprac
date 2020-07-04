# 131. Palindrome Partitioning
"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.
"""
#-------------------------------------------------------------------------------
#    Approach- 
#-------------------------------------------------------------------------------

#Dijkstra's 

#-------------------------------------------------------------------------------
#    Soluton  - DFS
#-------------------------------------------------------------------------------
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.dfs(s, [])
        return self.res
    
    def dfs(self, s, temp):
        # return condition
        if not s:
            self.res.append(temp[:]) # making copy not change the reference
            return
        
        # backtracking
        for i in range(1, len(s) + 1):
            if self.isPali(s[:i]):
                temp.append(s[:i])
                self.dfs(s[i:], temp)
                temp.pop()
        
    def isPali(self, s):
        return s == s[::-1]

#-------------------------------------------------------------------------------
#    test
#-------------------------------------------------------------------------------
# soln = Solution()
# print(soln.)