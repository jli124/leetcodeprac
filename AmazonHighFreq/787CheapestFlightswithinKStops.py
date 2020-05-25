# 787.  Cheapest Flights Within K Stops
"""
There are n cities connected by m flights. Each flight starts from city u and 
arrives at v with a price w.
"""
#-------------------------------------------------------------------------------
#    Approach- 
#-------------------------------------------------------------------------------

#Dijkstra's 

#-------------------------------------------------------------------------------
#    Soluton  - Dijkstra O(E + nlogn)
#-------------------------------------------------------------------------------
import collections 
import heapq
class Solution():
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        f = collections.defaultdict(dict)
        for a, b, p in flights:
            f[a][b] = p
        heap = [(0, src, k + 1)]
        while heap:
            # p: price needed to go from src to i
            p, i, k = heapq.heappop(heap)
            if i == dst:
                return p
            if k > 0:
                for j in f[i]:
                    # update price with f[i][j] when reaches j and costs one stop
                    heapq.heappush(heap, (p + f[i][j], j, k - 1))
        return -1

#-------------------------------------------------------------------------------
#    test
#-------------------------------------------------------------------------------
soln = Solution()
print(soln.findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,1))