# 81. Binary Search
"""
Given a sorted (in ascending order) integer array nums of n elements and a target value, 
write a function to search target in nums. If target exists, then return its index, otherwise return -1.
"""
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Binary search

"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False
        def search_rec(left, up, right, down):
            # if submatrix has no width or height
            if left > right or up > down:
                return False
            
            # if target is outside the range of the given numbers
            elif target < matrix[up][left] or target > matrix[down][right]:
                return False
            
            mid = left + (right - left) // 2
            row = up
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target: 
                    return True
                row += 1
            return search_rec(left, row, mid - 1, down) or search_rec(mid + 1, up, right, row - 1)
                
        R, C = len(matrix), len(matrix[0])
        return search_rec(0,0,C - 1,R - 1)
        
                    
#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

