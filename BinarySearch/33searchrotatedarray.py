# 33. Search in Rotated Sorted Array
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Binary search

"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) -1
        while left <= right:
            mid = left + right >> 1
            if nums[mid] == target:
                return mid
            
            if (target < nums[0] and not target < nums[mid] < nums[0] or
                    target >= nums[0] and nums[0] <= nums[mid] < target):
                left = mid +1
            else:
                right = mid -1
        return -1        

#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

