# 215. Kth Largest Element in an Array
"""
Find the kth largest element in an unsorted array. 
Note that it is the kth largest element in the sorted order, not the kth distinct element.
"""
#-------------------------------------------------------------------------------
#    Approach- 
#-------------------------------------------------------------------------------

"""
sorting
heap
"""

#-------------------------------------------------------------------------------
#    Soluton1 - sorting O(nk)
#-------------------------------------------------------------------------------
import heapq
# class Solution():
#     def findKthLargest(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         # only need to sort till k
        for i in xrange(len(nums), len(nums) - k, -1):
            tmp = 0
            # for element before index i, find the max and put at i-1 position
            for j in xrange(i):
                if nums[j] > nums[tmp]:
                    tmp = j
                    nums[tmp], nums[i-1] = nums[i-1], nums[tmp]
            return nums[len(nums) - k]

        
                    
        
#-------------------------------------------------------------------------------
#    Soluton2 - min-heap
#-------------------------------------------------------------------------------
class Solution():
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        for _ in xrange(len(nums) - k):
            heapq.heappop(heap)
        return heapq.heappop(heap)

        #return heapq.nlargest(k, nums)[k-1]

#-------------------------------------------------------------------------------
#    test
#-------------------------------------------------------------------------------
nums = [3,2,1,5,6,4]
k =2 
soln = Solution()
print(soln.findKthLargest(nums,k))