
# 154. Find Minimum in Rotated Sorted Array II

"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.
"""
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
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) / 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1
        return nums[left]
        

#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------
n = 5
soln = Solution()
print(soln.firstBadVersion(n))
