# 621. Task Scheduler
"""
Given a char array representing tasks CPU need to do. It contains capital letters
 A to Z where different letters represent different tasks. Tasks could be done 
 without original order. Each task could be done in one interval. For each interval,
CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, 
there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

"""
#-------------------------------------------------------------------------------
#    Approach- 
#-------------------------------------------------------------------------------

"""
stack 
"""

#-------------------------------------------------------------------------------
#    Soluton1 
#-------------------------------------------------------------------------------
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        n += 1
        ans = 0
        d = collections.Counter(tasks)
        heap = [-c for c in d.values()]
        heapq.heapify(heap)
        while heap:
            stack = []
            cnt = 0
            for _ in range(n):
                if heap:
                    c = heapq.heappop(heap)
                    cnt += 1
                    if c < -1:
                        stack.append(c + 1)
            for item in stack:
                heapq.heappush(heap, item)
            ans += heap and n or cnt
        return ans
        
                    
        
#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

