# 268. Missing Number
"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
find the one that is missing from the array.

"""
#-------------------------------------------------------------------------------
#    Approach- 
#-------------------------------------------------------------------------------

# Hashset
#-------------------------------------------------------------------------------
#    Soluton1  - Hashset -- O(n)
#-------------------------------------------------------------------------------
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        n = len(nums) + 1
        for num in range(n):
            if num not in num_set:
                return num
#-------------------------------------------------------------------------------
#    Soluton2  - Sorted -- O(nlogn)
#-------------------------------------------------------------------------------
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
    	nums.sort()
    	# edge 1, 0 is not in the list
    	if nums[0] != 0:
    		return 0
    	# edge 2, the last num is not in the list
    	elif nums[-1] != len(nums):
    		return len(nums)

    	for i in range(1, len(nums)):
    		expect_num = nums[i - 1] + 1
    		if nums[i] != expect_num:
    			return expect_num
#-------------------------------------------------------------------------------
#    test
#-------------------------------------------------------------------------------
# soln = Solution()
# print(soln.)