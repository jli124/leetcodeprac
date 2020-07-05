# 17. Letter Combinations of a Phone Number
"""
Given a string containing digits from 2-9 inclusive, return all possible letter 
combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.
"""
#-------------------------------------------------------------------------------
#    Approach- 
#-------------------------------------------------------------------------------

#DFS

#-------------------------------------------------------------------------------
#    Soluton  - XOR and hashmap
#-------------------------------------------------------------------------------
class Solution:
    def letterCombinations(self, string: str) -> List[str]:
        # edge case
        if not string:
            return []
        
        # global variable
        self.dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'  
        }
        self.res = []
        
        # dfs helper function
        def dfs(string, index, temp):
            if len(string) == len(temp):
                self.res.append("".join(x for x in temp))
                return
            
            for char in self.dict[string[index]]: 
                dfs(string, index+1, temp)      
        
        # function call
        dfs(string, 0, [])
        return self.res

#-------------------------------------------------------------------------------
#    test
#-------------------------------------------------------------------------------
# soln = Solution()
# print(soln.)