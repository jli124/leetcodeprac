#133. Clone Graph
#Given a reference of a node in a connected undirected graph.
#Return a deep copy (clone) of the graph.
#Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. node -> nodes
2. copy nodes
3. copy edges (mapping relations)
Breadth first search + queue could be used 
"""

#-------------------------------------------------------------------------------
#    Soluton1 --- BFS and key-value pair for node and clone of it
#-------------------------------------------------------------------------------
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
from collections import deque
class Solution(object):
        
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node
        # dictionary used to save visited node and clone as key value pair.
        visited = {}
        
        # put the first node into the queue
        queue = deque([node])
        # Clone the node and put it in the visited dictionary
        visited[node] = Node(node.val,[])
        
        # Start BFS traversal
        while queue:
            # Pop a node from the front of the queue
            n = queue.popleft()
            # Iterate through all neighbours of the node
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val,[])
                    queue.append(neighbor)
                    
                # Add the clone of the neighbor to the neighbors of the clone node "n"   
                visited[n].neighbors.append(visited[neighbor])
        return visited[node]
#-------------------------------------------------------------------------------
#    Soluton2 ---Recursive
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

