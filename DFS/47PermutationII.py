#47 Permutations II
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
DFS
"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            
        for i in range(len(nums)):   
            if i>0 and nums[i - 1] == nums[i]: 
                continue
            self.dfs(nums[:i]+nums[i+1:], path + [nums[i]], res)

#-------------------------------------------------------------------------------
#    Solution 2 - BackTrack
#-------------------------------------------------------------------------------
