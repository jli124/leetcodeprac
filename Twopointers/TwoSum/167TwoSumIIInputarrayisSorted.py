## 167. Two Sum II - Input array is sorted
# Given an array of integers that is already sorted in ascending order, find two numbers 
# such that they add up to a specific target number.
# The function twoSum should return indices of the two numbers such that they add up to 
# the target, where index1 must be less than index2
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Two pointer

"""

#-------------------------------------------------------------------------------
#    Soluton1 
#-------------------------------------------------------------------------------
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(nums)-1
        res = []
        while left < right:
            if nums[left] + nums[right] == target:
                res.append(left + 1)
                res.append(right + 1)
                left += 1
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
                
        return res

#-------------------------------------------------------------------------------
#    Solution2 
#-------------------------------------------------------------------------------


nums= [2,7,11,15]

soln = Solution()
print(soln.triangleNumber(nums))