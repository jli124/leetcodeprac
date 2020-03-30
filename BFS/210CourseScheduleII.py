# 210 Course Schedule II
"""
#-------------------------------------------------------------------------------
#    Approach- 
#-------------------------------------------------------------------------------

"""

"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------
from collections import defaultdict
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # use dict to keep course:neighbours
        dic = {i:set() for i in xrange(numCourses)}
        neigh = collections.defaultdict(set)
        
        for i,j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        
        # queue stores the courses have no prerequisite
        queue = collections.deque([i for i in dic if not dic[i]])
        count, res = 0, []
        while queue:
            node = queue.popleft()
            res.append(node)
            # use count check whether it could be sorted by topological sorting
            count += 1
            for i in neigh[node]:
                dic[i].remove(node)
                # if there is no prerequisite for i then add to queue
                if not dic[i]:
                    queue.append(i)
        return res if count==numCourses else []    
        
#-------------------------------------------------------------------------------
#    Soluton2 
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
#    test
#-------------------------------------------------------------------------------
