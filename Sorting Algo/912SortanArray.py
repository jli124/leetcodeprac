#912. Sort an array
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
use merge sort
"""

#-------------------------------------------------------------------------------
#    Implementation
#-------------------------------------------------------------------------------
class Solution(object):
    def sortArray(self, A):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = [0 for _ in range(len(A))]
        self.merge_sort(0, len(A) - 1, A, temp)
        return A
        
    def merge_sort(self, start, end, A, temp):
        if start >= end:
            return
        
        mid = (start + end) / 2
        self.merge_sort(start, mid , A, temp)
        self.merge_sort(mid + 1, end, A, temp)
        self.merge(start, mid, end, A, temp)
        
    def merge(self, start, mid, end, A, temp):
        left, right = start, mid + 1
        index = start
        while left <= mid and right <= end:
            if A[left] < A[right]:
                temp[index] = A[left]
                left += 1
            else:
                temp[index] = A[right];
                right += 1
                
            index += 1
            
        while left <= mid:
            temp[index] = A[left]
            left += 1
            index += 1
            
        while right <= end:
            temp[index] = A[right]
            right += 1
            index += 1
            
        for index in range(start, end + 1):
            A[index] = temp[index]