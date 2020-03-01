#349. Intersection of Two Arrays
# Given two arrays, write a function to compute their intersection.
# #-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Two pointers, start from the end
"""

#-------------------------------------------------------------------------------
#    Soluton - O(m+n) and O(1)
#-------------------------------------------------------------------------------

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # two pointers for num1 and num2 as well as the point for num1(in-place)
        p1, p2, p = m-1, n-1, m + n - 1
        
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
            
        # add missing elements from num2 if n > m
        nums1[:p2 + 1] = nums2[:p2 + 1]