# 137. Single Number II
"""
Given a non-empty array of integers, every element appears three times except for one, 
which appears exactly once. Find that single one.
"""
#-------------------------------------------------------------------------------
#    Approach- 
#-------------------------------------------------------------------------------

#Hashmap

#-------------------------------------------------------------------------------
#    Soluton  - XOR and hashmap
#-------------------------------------------------------------------------------
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = {}
        
        for num in nums:
            dict[num] = dict.get(num, 0) + 1
        
        for key, val in dict.items():
            if val == 1:
                return key

#-------------------------------------------------------------------------------
#    test
#-------------------------------------------------------------------------------
# soln = Solution()
# print(soln.)