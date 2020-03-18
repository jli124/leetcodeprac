# 785. Is Graph Bipartite?
"""
Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent 
subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for 
which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  
There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

 
"""
#-------------------------------------------------------------------------------
#    Approach- 
#-------------------------------------------------------------------------------

"""
bfs
"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------
import collections 
class Solution():
    def isBipartite(self, graph):
            """
            :type graph: List[List[int]]
            :rtype: bool
            """
            n, colored = len(graph), {}
            for i in range(n):
                if i not in colored and graph[i]:
                    colored[i] = 1
                    q = collections.deque([i])
                    print(colored)
                    print(q)
                    while q:
                        cur = q.popleft()
                        for nb in graph[cur]:
                            if nb not in colored:
                                colored[nb] = -colored[cur]
                                q.append(nb)
                            elif colored[nb] == colored[cur]:
                                return False
            return True

#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------
graph =[[1,3], [0,2], [1,3], [0,2]]
soln = Solution()
print(soln.isBipartite(graph))
#-------------------------------------------------------------------------------
#    test
#-------------------------------------------------------------------------------
