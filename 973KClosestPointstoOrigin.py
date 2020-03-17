# 973. K Closest Points to Origin
"""
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
(Here, the distance between two points on a plane is the Euclidean distance.)
You may return the answer in any order.  The answer is guaranteed to be unique 
(except for the order that it is in.)
"""
#-------------------------------------------------------------------------------
#    Approach- 
#-------------------------------------------------------------------------------

"""
sorting
heap
"""

#-------------------------------------------------------------------------------
#    Soluton1 - sorting O9(nlogn)
#-------------------------------------------------------------------------------
# class Solution(object):
#     def kClosest(self, points, K):
#         """
#         :type points: List[List[int]]
#         :type K: int
#         :rtype: List[List[int]]
#         """
#         points.sort(key= lambda P:P[0]**2 + P[1]**2)
#         return points[:K]
        
                    
        
#-------------------------------------------------------------------------------
#    Soluton2 - Quick Sort
#-------------------------------------------------------------------------------
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        # points.sort(key= lambda P:P[0]**2 + P[1]**2)
        # return points[:K]
        # quick sort
        self.sort(points, 0, len(points) - 1, K)
        return points[:K]
    
    def sort(self, points, l, r, K):
        if l < r:
            p = self.partition(points, l, r)
            if p == K:
                return
            elif p < K:
                self.sort(points, p+1, r, K)
            else:
                self.sort(points,l,p-1,K)
        
    
    def partition(self, points, l, r):
        pivot = points[r]
        a = l
        for i in range(l,r):
            if (points[i][0]**2 + points[i][1]**2 <= pivot[0]**2 + pivot[1]**2):
                points[a], points[i] = points[i], points[a]
                a += 1
        points[a], points[r] = points[r], points[a]
        return a

#-------------------------------------------------------------------------------
#    test
#-------------------------------------------------------------------------------
points = [[1,3],[-2,2]]
K = 1
soln = Solution()
print(soln.kClosest(points,K))