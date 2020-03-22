# 33. Search in Rotated Sorted Array
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Binary search

"""

#-------------------------------------------------------------------------------
#    Soluton - logN
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
            # case 1 target found
            if target == nums[mid]:
                return mid
            if target < nums[0]:
                if target < nums[mid] < nums[0]:
                    right = mid -1
                else:
                    left = mid +1
            ## target >= nums[0]
            else:
                if nums[0] <= nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid -1
        return -1       

#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

