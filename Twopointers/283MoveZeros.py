# 283. Move Zeroes
# Given an array nums, write a function to move all 0's to the end of it while 
# maintaining the relative order of the non-zero elements.
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Two pointers

"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ptr1 = 0
        for ptr2 in xrange(len(nums)):
        	if nums[ptr2] != 0:
        		nums[ptr2], nums[ptr1] = nums[ptr1], nums[ptr2]
        		ptr1 += 1
        return nums




                         

#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

