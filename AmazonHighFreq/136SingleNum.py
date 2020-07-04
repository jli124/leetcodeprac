# 136. Single Number
"""
Given a non-empty array of integers, every element appears twice except for one. 
Find that single one.
"""
#-------------------------------------------------------------------------------
#    Approach- 
#-------------------------------------------------------------------------------

#XOR is better than hashmap

#-------------------------------------------------------------------------------
#    Soluton  - XOR and hashmap
#-------------------------------------------------------------------------------
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = {}
        for num in nums:
            # if num not in the key of dict, set it to 0 o.w. + 1
            dict[num] = dict.get(num, 0) + 1
            
        for key, val in dict.items():
            if val == 1:
                return key


 #-------------------------------------------------------------------------------
#    Soluton 2 - XOR 
#-------------------------------------------------------------------------------
class Solution:
    def singleNumber(self, nums: List[int]) -> int:  
        res = 0
        for num in nums:
            res ^= num
        return res    
#-------------------------------------------------------------------------------
#    test
#-------------------------------------------------------------------------------
# soln = Solution()
# print(soln.)