# 1046. Last Stone Weight
"""
We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose the two heaviest rocks and smash them together.  Suppose the stones have weights x 
and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

"""
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
heap: push to the top, pop the minimum
+ set for uniqueness
"""

#-------------------------------------------------------------------------------
#    Soluton1
#-------------------------------------------------------------------------------
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-1*i for i in stones]
        while len(stones) > 1:
            heapq.heapify(stones)
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            if s1 != s2:
                heapq.heappush(stones, s1 - s2)
        return -1*stones[0] if stones else 0
#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

