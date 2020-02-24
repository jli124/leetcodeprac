#78. Subsets
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Number of subset: 2^n
"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
            
        return output
#-------------------------------------------------------------------------------
#    Solution 2 - BackTrack
#-------------------------------------------------------------------------------
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    def backtrack(first= 0, curr = []):
        if len(curr) == k:
            output.append(curr[:])
        for i in range(first, n):
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()
        
    output = []
    n = len(nums)
    for k in range(n+1):
        backtrack()
    return output