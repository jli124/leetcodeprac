# 1197. Minimum Knight Moves
"""
In an infinite chess board with coordinates from -infinity to +infinity, you have a
 knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two 
squares in a cardinal direction, then one square in an orthogonal direction.
"""

#-------------------------------------------------------------------------------
#    Approach- 
#-------------------------------------------------------------------------------
"""
BFS
"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------
class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if x == 0 and y == 0:
            return 0
        return self.bfs(abs(x), abs(y))


    def bfs(self, x, y):
        moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        q = [(0, 0, 0)]
        visited = set()
        visited.add((0, 0)) 
        while len(q) > 0:
            i, j, dis = q.pop(0)
            for move in moves:
                a, b = i + move[0], j + move[1]
                if (a,b) not in visited and a >= -5 and b >= -5:
                    if a == x and b == y:
                        return dis + 1
                    q.append((a, b, dis+1))
                    visited.add((a, b))
            
        
        
#-------------------------------------------------------------------------------
#    Soluton2 
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
#    test
#-------------------------------------------------------------------------------
