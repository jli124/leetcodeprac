#350. Intersection of Two ArraysII
# Given two arrays, write a function to compute their intersection. (could have duplicaates)
# #-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Hashmap
"""

#-------------------------------------------------------------------------------
#    Soluton - O(m+n) and O(1)
#-------------------------------------------------------------------------------

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        nums_dict = {}
        #for every value in nums1 store it in the dictionary
        for num in nums1:
            nums_dict[num] =nums_dict[num] + 1 if num in nums_dict else 1
        # for every value in nums2 check if it is in dict, if it is append it to the res
        for num in nums2:
            if num in nums_dict and nums_dict[num] > 0:
                res.append(num)
                nums_dict[num] -= 1
        
        return res