# 973. K Closest Points to Origin
"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to 
first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, 
return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. 
If it is impossible to finish all courses, return an empty array.
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
            count += 1
            for i in neigh[node]:
                dic[i].remove(node)
                if not dic[i]:
                    queue.append(i)
        return res if count==numCourses else []
        
                    
        
#-------------------------------------------------------------------------------
#    Soluton2 
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
#    test
#-------------------------------------------------------------------------------
