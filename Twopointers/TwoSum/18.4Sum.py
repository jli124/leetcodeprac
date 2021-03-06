## 18. 4Sum
# Given an array nums of n integers and an integer target, are there elements a, b, c, 
# and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array 
# which gives the sum of target.
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Two pointer + recursion

"""

#-------------------------------------------------------------------------------
#    Soluton1 
#-------------------------------------------------------------------------------
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def findNsum(nums, target, N, result, results):
            #early termination
            if N < 2 or N > len(nums) or target < nums[0]*N or target > nums[-1]*N:
                return
            
            # use two pointer for two sum questions
            if N == 2:
                l, r = 0, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    
                    elif s < target:
                        l += 1
                    
                    else:
                        r -= 1
            
            # recursively reduce N
            else:
                for i in range(len(nums)-(N-1)):
                    if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                        findNsum(nums[i+1:], target - nums[i], N-1, result+[nums[i]], results)
                        
        results = []
        findNsum(sorted(nums), target, 4, [], results)
        return results
        

#-------------------------------------------------------------------------------
#    Test 
#-------------------------------------------------------------------------------
nums = [-1, 2, 1, -4]
target = 1

soln = Solution()
print(soln.threeSumClosest(nums,target))