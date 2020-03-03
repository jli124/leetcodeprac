## 16. 3Sum Closest
# Given an array nums of n integers and an integer target, find three integers in nums 
# such that the sum is closest to target. Return the sum of the three integers. 
# You may assume that each input would have exactly one solution.
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
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            l, r = i+1, len(nums) - 1
            while l < r:
                sum3 = nums[i] + nums[l] + nums[r]
                ##found the target if sum equals to target
                if sum3 == target:
                    return sum3
                ## sum smaller than target, left pointer moves forward
                elif sum3 < target:
                    l += 1
                ## sum bigger than target, right moves to the left
                else:
                    r -= 1
                ##return the closest one
                if abs(sum3 - target) < abs(result - target):
                    result = sum3
            
        return result
        

#-------------------------------------------------------------------------------
#    Test 
#-------------------------------------------------------------------------------
nums = [-1, 2, 1, -4]
target = 1

soln = Solution()
print(soln.threeSumClosest(nums,target))