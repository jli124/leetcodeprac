# 26. Remove Duplicates from Sorted Array
# Given a sorted array nums, remove the duplicates in-place such that each element 
# appear only once and return the new length.Do not allocate extra space for another 
# array, you must do this by modifying the input array in-place with O(1) extra memory.
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Hashmap
if not extra space, then two pointers

"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zero = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[zero]:
                zero += 1
                nums[zero] = nums[i]
        return zero+1



                         

#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

