# 238. Product of Array Except Self
"""
Given an array nums of n integers where n > 1,  return an array output such that 
output[i] is equal to the product of all the elements of nums except nums[i].
"""
#-------------------------------------------------------------------------------
#    Approach- 
#-------------------------------------------------------------------------------

"""
Input = [1, 2, 3, 4]
L = [1, 2, 6, 24]
R = [6, 12, 4, 1]
answer = L*R (element wise) = [24, 12, 8, 6]
"""

#-------------------------------------------------------------------------------
#    Soluton 1 
#-------------------------------------------------------------------------------
class Solution(object):  
    def productExceptSelf(self, nums):
        length = len(nums)
        L, R, answer = [0]*length, [0]*length, [0]*length
        
        #create L list = [1, 2, 6, 24]
        L[0] = 1
        for i in range(1, length):
            L[i] = L[i-1] * nums[i-1]
        # create R = [6, 12, 4, 1]
        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            R[i] = R[i+1] * nums[i+1]
        # calculate answer + L * R
        for i in range(length):
            answer[i] = L[i] * R[i]
            
        return answer        
        


#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------
nums = [1, 2, 3, 4]
soln = Solution()
print(soln.productExceptSelf(nums))
#-------------------------------------------------------------------------------
#    test
#-------------------------------------------------------------------------------
