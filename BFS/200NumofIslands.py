# 200. Number of Islands
"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally 
or vertically. You may assume all four edges of the grid are all surrounded by water.
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
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid,i,j)
                    count += 1
        return count
    
    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] ='#'
        self.dfs(grid,i-1,j)
        self.dfs(grid,i+1,j)
        self.dfs(grid,i,j-1)
        self.dfs(grid,i,j+1)
 
        
#-------------------------------------------------------------------------------
#    Soluton2 
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
#    test
#-------------------------------------------------------------------------------
