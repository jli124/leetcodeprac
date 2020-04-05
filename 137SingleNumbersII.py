# 137. Single Number II
"""
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
"""
#-------------------------------------------------------------------------------
#    Approach- 
#-------------------------------------------------------------------------------

"""

"""

#-------------------------------------------------------------------------------
#    Soluton 1 - Set
#-------------------------------------------------------------------------------
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (3* sum(set(nums)) - sum(nums)) // 2



#-------------------------------------------------------------------------------
#    Solution 2 - Dict
#-------------------------------------------------------------------------------
class Solution(object):
	from collections import Counter
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res_dict = Counter(nums)

        for num in nums:
        	if res_dict[num] == 1:
        		return num

#-------------------------------------------------------------------------------
#    Solution 3 - XOR
#-------------------------------------------------------------------------------
class Solution(object):
	from collections import Counter
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda a, b (a ^ b))

#-------------------------------------------------------------------------------
#    test
#-------------------------------------------------------------------------------
