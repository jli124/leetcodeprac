# 240 Search in 2D Matrix II
"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
"""
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Binary search - D&C 

"""

#-------------------------------------------------------------------------------
#    Soluton - DC O(nlgn)
#-------------------------------------------------------------------------------
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        
        def search_rec(up, left, down, right):
            #submatrix has no width and height
            if left > right or up > down:
                return False
            
            # target is outside the range of the submatrix
            elif target < matrix[up][left] or target > matrix[down][right]:
                return False
            
            mid = left + (right - left) // 2
            # locate row s.t. matrix[row-1][mid] < target < matrix[row][mid]
            
            row = up
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
            
            # divide into left bottom sutmat and upper right submat
            return search_rec(row, left, down, mid - 1) or search_rec(up,mid + 1, row-1, right)
        
        return search_rec(0,0,len(matrix) - 1, len(matrix[0]) - 1)
            
        
                    
#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

