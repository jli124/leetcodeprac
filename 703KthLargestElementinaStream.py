# 703. Kth Largest Element in a Stream
"""
Design a class to find the kth largest element in a stream. Note that it is the 
kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and 
an integer array nums, which contains initial elements from the stream. 
For each call to the method KthLargest.add, return the element representing 
the kth largest element in the stream.


"""
#-------------------------------------------------------------------------------
#    Approach- O(klogn)
#-------------------------------------------------------------------------------

"""
Maxheap
-create heap keeping only the k-largest elements by poping off small elements
-if new vale bigger than the smallest element, then it will be added to the heap
"""

#-------------------------------------------------------------------------------
#    Soluton1 
#-------------------------------------------------------------------------------
import heapq
class KthLargest():

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        print(self.pool)
        while len(self.pool) > k:
            heapq.heappop(self.pool)
        print(self.pool)
            
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]
                
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

k = 3
nums = [4,5,8,2]
klst = KthLargest(k,nums)
print(klst.add(3))