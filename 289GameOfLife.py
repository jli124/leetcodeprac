# 289. Game of Life
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Array

"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        neighbors = [(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1)]
        
        rows = len(board)
        cols = len(board[0])
        
        '''
        1 - cell is alive
        0 - cell is dead
       -1 - alive -> dead
        2 - dead -> alive
        '''
        
        for row in range(rows):
            for col in range(cols):
                ## Calculating live neighbors for each cell
                live_neighbors = 0
                for neighbor in neighbors:
                    r = row + neighbor[0]
                    c = col + neighbor[1]
                    
                    if 0 <= r < rows and 0 <= c < cols and abs(board[r][c]) == 1:
                        live_neighbors += 1
                        
                ## Rule 1 and 3
                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors >3):
                    board[row][col] = -1
                # Rule 4
                if board[row][col] == 0 and live_neighbors ==3:
                    board[row][col] = 2
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] > 0: board[row][col] =1
                else:
                    board[row][col] = 0
                         

#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

