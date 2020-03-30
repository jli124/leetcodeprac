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
topological order, bfs
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
        edges = [[] for i in range(numCourses)]  # use edge to store the relationship between the two courses
        indegrees = [0] * numCourses # use degrees (list) to store the indegree of the courses in order
        for course, precourse in prerequisites:
            edges[precourse].append(course)
            indegrees[course] += 1

        # add the queue to the initial queue if the course has indegree of 0
        queue = collections.deque(course for course, indegree in enumerate(indegrees) if not indegree)
        while queue:
            course = queue.popleft()
            for next_course in edges[course]:
                # after checking the previous level of courses, process to next level and  - 1
                indegrees[next_course] -= 1
                # if the indegree is equal to 0 add to the queue
                if not indegrees[next_course]:
                    queue.append(next_course)

        return not sum(indegrees)

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
