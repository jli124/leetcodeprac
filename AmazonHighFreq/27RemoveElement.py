# 268. Missing Number
"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
find the one that is missing from the array.

"""
#-------------------------------------------------------------------------------
#    Approach- 
#-------------------------------------------------------------------------------

# Two Pointer

#-------------------------------------------------------------------------------
#    Soluton1  - Two Pointer
#-------------------------------------------------------------------------------
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # for num in reversed(nums):
        #     if num == val:
        #         nums.remove(num)
        # return len(nums)
        left, right = 0 , len(nums) - 1
        while left <= right:
            if nums[left] == val:
                nums[left], nums[right], right = nums[right], nums[left], right - 1
            else:
                left += 1
        return left
#-------------------------------------------------------------------------------
#    test
#-------------------------------------------------------------------------------
# soln = Solution()
# print(soln.)