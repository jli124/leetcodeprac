# 81. Search in Rotated Sorted Array II
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
# You are given a target value to search. If found in the array return true, otherwise 
# return false.
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
        :rtype: bool
        """
        if not nums:
            return False
        
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            
            if nums[mid] == target:
                return True
            #second half is ordered
            if nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            # first half is ordered       
            elif nums[mid] > nums[r]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            #moves the right pointer one step forward when nums[mid] == nums[r],
            else:
                r -= 1
        return nums[l] == target 

#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

