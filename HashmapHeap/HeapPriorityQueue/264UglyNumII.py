# 264. Ugly Number II
"""
Write a program to find the n-th ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
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
from heapq import heappop, heappush
class Ugly:
    def __init__(self):
        seen = {1,}
        self.nums = nums = []
        heap = []
        heappush(heap,1)
        
        for _ in range(1690):
            curr_ugly = heappop(heap)
            nums.append(curr_ugly)
            for i in [2, 3, 5]:
                new_ugly = curr_ugly * i
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heappush(heap, new_ugly)        
        
class Solution:
    u = Ugly()
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.u.nums[n - 1]
        
#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

