# 444. Sequence Reconstruction

#-------------------------------------------------------------------------------
#    Approach- 
#-------------------------------------------------------------------------------

"""
topological sorting

"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------
class Solution(object):
    from collections import deque
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        if len(org) <= 0 :
            return False
        
        sortedOrder = []
        
        #1. Initialize the graph keeping check of indegree and the adajacent list
        inDegree, graph = {}, {}
        for seq in seqs:
            for num in seq:
                inDegree[num] = 0
                graph[num]  = []
        
        #2. Build the graph
        for seq in seqs:
            for indx in range(len(seq) - 1):
                parent, child = seq[indx], seq[indx + 1]
                graph[parent].append(child)
                inDegree[child] += 1
        
        if len(inDegree) != len(org):
            return False
        
        #3. Find all sources, add vertices w/ indegree is 0 using BFS
        sources = deque()
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)
        
        #4. Add t othe sortedOrder list, - indegree for all children
        # if indegree is o, add to the queue (sources)
        while sources:
            # if there is more than one way of construction
            if len(sources) > 1: return False
            # the next source(or number) is different from the original sequence
            if org[len(sortedOrder)] != sources[0]: return False
            
            vertex = sources.popleft()
            sortedOrder.append(vertex)
            for child in graph[vertex]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)
        
        return len(sortedOrder) == len(org)
                
 
        
#-------------------------------------------------------------------------------
#    Soluton2 
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
#    test
#-------------------------------------------------------------------------------
