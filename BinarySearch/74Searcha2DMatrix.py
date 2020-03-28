# 74. Search a 2D Matrix
"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
"""
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Binary search

"""

#-------------------------------------------------------------------------------
#    Soluton1 O(logmn)
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
        
        row_num, col_num = len(matrix), len(matrix[0])
        low, high = 0, row_num * col_num
        
        while low < high:
            mid = low + (high - low) / 2
            x = matrix[mid/col_num][mid%col_num]
            if x < target:
                low = mid + 1
            elif x > target:
                high = mid
            else:
                return True
        return False
        
                    
#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

