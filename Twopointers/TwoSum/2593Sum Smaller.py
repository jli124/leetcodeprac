## 259. 3Sum Smaller
# Given an array of n integers nums and a target, find the number of index triplets 
# i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.
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
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        
        # define a helper function calculate two-sum question by using two pointer
        def twoSumSmaller(nums,startind,target):
            left, right = startind, len(nums) - 1
            sum_res = 0
            while left < right:
                if nums[left] + nums[right] < target:
                    sum_res += right - left
                    left += 1
                else:
                    right -= 1
            return sum_res
        
        # iterate through the list and use twosum function to find the final result
        res = 0
        for i in range(len(nums) - 2):
            res += twoSumSmaller(nums,i+1,target - nums[i])
            
        return res

#-------------------------------------------------------------------------------
#    Solution2 
#-------------------------------------------------------------------------------


nums= [2,7,11,15]

soln = Solution()
print(soln.triangleNumber(nums))