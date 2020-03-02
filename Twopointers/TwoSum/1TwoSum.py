# 796. Rotate String
# Given an array of integers, return indices of the two numbers such that they add 
# up to a specific target.You may assume that each input would have exactly one 
# solution, and you may not use the same element twice.
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1.Hashmap

"""

#-------------------------------------------------------------------------------
#    Soluton1 - Hashmap O(n) & o(n)
#-------------------------------------------------------------------------------
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i,num in enumerate(nums):
            remaining = target - num
            if remaining not in seen:
                seen[num] = i
            else:
                return [seen[remaining],i]

#-------------------------------------------------------------------------------
#    Solution2 
#-------------------------------------------------------------------------------


