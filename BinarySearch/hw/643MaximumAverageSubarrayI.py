#643. Maximum Average Subarray I
"""
Given an array consisting of n integers, find the contiguous subarray of given 
length k that has the maximum average value. And you need to output the maximum average value.

"""

#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Binary Search

"""

#-------------------------------------------------------------------------------
#    Soluton1 
#-------------------------------------------------------------------------------
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
    
        curr_sum = 0
        for i in range(k):
            curr_sum += nums[i]
        res = curr_sum
        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i - k]
            res = max(res, curr_sum)
        return res/float(k)
        
#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

