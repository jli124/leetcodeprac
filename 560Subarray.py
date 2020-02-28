# 560. Subarray Sum Equals K
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
hashmap

"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # using hashmap to store cumulative sum (cur)
        # and if cur - target (k) occurs already, res + 1
        count, cur, res = {0:1}, 0, 0
        for v in nums:
            cur += v
            res += count.get(cur - k, 0)
            count[cur] = count.get(cur, 0) + 1
        return res
        


                         

#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

