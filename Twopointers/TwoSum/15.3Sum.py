## 15. 3Sum
# Given an array nums of n integers, are there elements a, b, c in nums such that 
# a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
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
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        
        for i in range(len(nums)-2):
            ## find unique triplets
            if i>0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums) - 1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                #three_sum == 0:
                else:
                    res.append((nums[l], nums[i], nums[r]))
                    # get rid of duplicates
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
                    
        return res
        

#-------------------------------------------------------------------------------
#    Solution2 
#-------------------------------------------------------------------------------


nums= [-1,0,1,2,-1,-4]

soln = Solution()
print(soln.threeSum(nums))