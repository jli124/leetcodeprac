#90. SubsetsII
"""
Given a collection of integers that might contain duplicates, nums, 
return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.
"""
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""

"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.dfs(nums, 0 , [], res)
        return res
        
    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index,len(nums)):
            if i> index and nums[i] == nums[i-1]: 
                continue
            self.dfs(nums, i+1, path+[nums[i]],res )
