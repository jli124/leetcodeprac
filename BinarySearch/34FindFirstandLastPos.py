

# 278. First Bad Version
"""
Given an array of integers nums sorted in ascending order, find the starting and 
ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].
"""
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Binary search * 2

"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = self.search(target, nums)
        #find the next number in the arr and return the pos - 1
        if target in nums[first:first+2]:
            return [first, self.search(target+1, nums)-1]
        # if it is not in the array return [-1,-1]
        else:
            return [-1, -1]
    
    # helper function to return the first position
    def search(self, n, nums):
        start, end = 0, len(nums)
        while start < end:
            mid = start + (end - start) / 2
            if nums[mid] > n:
                end = mid
            elif nums[mid] == n:
                end = mid
            else:
                start = mid + 1
        return start

        
        
        
        
             

#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------
n = 5
soln = Solution()
print(soln.firstBadVersion(n))
