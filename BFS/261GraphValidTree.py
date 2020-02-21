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
def validTree(self, n, edges):
    neighbors = {i: [] for i in range(n)}
    for v, w in edges:
        neighbors[v] += w,
        neighbors[w] += v,
    def visit(v):
        map(visit, neighbors.pop(v,[]))
    visit(0)
    ##check for n-1 edges and connectivity
    return len(edges) == n-1 and not neighbors

#-------------------------------------------------------------------------------
#    Soluton2 ---Recursive
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

