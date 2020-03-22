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
#    Solution 2 - Dfs
#-------------------------------------------------------------------------------
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i+1, path+[nums[i]], res)