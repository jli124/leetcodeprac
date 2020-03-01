#349. Intersection of Two Arrays
# Given two arrays, write a function to compute their intersection.
# #-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Two pointers, start from the end
"""

#-------------------------------------------------------------------------------
#    Soluton2 -  using set default method
#-------------------------------------------------------------------------------
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)

#-------------------------------------------------------------------------------
#    Soluton2 -  using hashmap
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
                nums_dict[num] = 0
        
        return res
#-----------------------------------------------------------------------------------------------
#    Soluton3 -  sort the two lists and use two pointer to search the lists for common elements
#-----------------------------------------------------------------------------------------------
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while (i < len(nums1) and j < len(nums2)):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                if not (len(res) and nums1[i] == res[len(res)-1]):
                    res.append(nums1[i])
                i += 1
                j += 1

        return res

