# 796. Rotate String
# Given an array with n objects colored red, white or blue, sort them in-place 
# so that objects of the same color are adjacent, with the colors in the order red, 
# white and blue.
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and 
# blue respectively.
# Note: You are not suppose to use the library's sort function for this problem.
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
M1: Use partition array twice
M2: count the times that 0, 1, 2 appear ---- Counting sort
    disadvantage: the keys have to be countable, for example: float is not countable
    
M3:

"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low, high = 0, len(nums) - 1
        i = 0
        def swap(nums,i,j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            
        while i <= high:
            if nums[i] == 0:
                swap(nums,low,i)
                low += 1
                i += 1
            elif nums[i] == 2:
                swap(nums,i,high)
                high -= 1
            else:
                i += 1


                         

#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

