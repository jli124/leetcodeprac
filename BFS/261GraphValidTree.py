#261. Graph Valid Tree
#Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
DFS, union-find
"""

#-------------------------------------------------------------------------------
#    Soluton1 ---DFS, adjacent list
#-------------------------------------------------------------------------------
class Solution():
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        neighbors = {i: [] for i in range(n)}

        for v, w in edges:
            neighbors[v] += w,
            neighbors[w] += v,
        print(neighbors) 

        def visit(v):
            map(visit, neighbors.pop(v,[]))
        visit(0)
        print(neighbors)
        ##check for n-1 edges and connectivity
        return len(edges) == n-1 and not neighbors

#-------------------------------------------------------------------------------
#    Soluton2 ---Recursive
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------
n = 5
edges = [[0,1], [0,2], [0,3], [1,4]]
soln = Solution()
print(soln.validTree(n,edges))
