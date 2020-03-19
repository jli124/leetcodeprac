# 332 Reconstruct Itinerary
"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], 
reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. 
Thus, the itinerary must begin with JFK.
 
"""
#-------------------------------------------------------------------------------
#    Approach- 
#-------------------------------------------------------------------------------

"""
DFS  + backtracking
"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------
from collections import defaultdict
class Solution():
    # def findItinerary(self, tickets):
    #     d = defaultdict(list)
    #     for flight in tickets:
    #         d[flight[0]] += flight[1],
    #     self.route = ['JFK']
    #     #print(d)
    #     def dfs(start = 'JFK'):
    #         ## find out the destinations that start with JFK
    #         myDsts = sorted(d[start])
    #         for dst in myDsts:
    #             d[start].remove(dst)
    #             self.route += dst,
    #             dfs(dst)
    #             if (len(self.route) == len(tickets) + 1):
    #                 return self.route
    #             # self.route.pop()
    #             # d[start] += dst,
    #     return dfs()
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        targets = defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route = []
        def dfs(airport):
            while targets[airport]:
                dfs(targets[airport].pop())
            route.append(airport)
        dfs('JFK')
        return route[::-1]

#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------
tickets =[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
soln = Solution()
print(soln.findItinerary(tickets))
#-------------------------------------------------------------------------------
#    test
#-------------------------------------------------------------------------------
