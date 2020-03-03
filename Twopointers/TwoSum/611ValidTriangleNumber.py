## 611. Valid Triangle Number
# Given an array consists of non-negative integers, your task is to count the number 
# of triplets chosen from the array that can make triangles if we take them as side 
# lengths of a triangle.
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
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        nums = nums[::-1]
        res= 0
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums) - 1
            while j < k:
                diff = nums[i] - nums[j]
                while nums[k] <= diff and k > j:
                    k -= 1
                res += k-j
                j += 1
        return res




        return nums[::-1]

#-------------------------------------------------------------------------------
#    Solution2 - Use two pointer O(nlogn) & o(1)
#-------------------------------------------------------------------------------


nums= [2,7,11,15]

soln = Solution()
print(soln.triangleNumber(nums))