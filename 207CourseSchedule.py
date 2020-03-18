# 207. Course Schedule
"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to 
first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, 
is it possible for you to finish all courses?

 
"""
#-------------------------------------------------------------------------------
#    Approach- 
#-------------------------------------------------------------------------------

"""
bfs
"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------
import collections 
class Solution():
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        edges = [[] for i in range(numCourses)]
        degrees = [0] * numCourses
        for course, precourse in prerequisites:
            edges[precourse].append(course)
            degrees[course] += 1

        queue = collections.deque(course for course, degree in enumerate(degrees) if not degree)
        while queue:
            course = queue.popleft()
            for next_course in edges[course]:
                degrees[next_course] -= 1
                if not degrees[next_course]:
                    queue.append(next_course)

        return not sum(degrees)

#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------
numCourses = 2 
prerequisites = [[1,0],[0,1]]
soln = Solution()
print(soln.canFinish(numCourses, prerequisites))
#-------------------------------------------------------------------------------
#    test
#-------------------------------------------------------------------------------
