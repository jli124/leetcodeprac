# 437. Path Sum III
#You are given a binary tree in which each node contains an integer value.
#Find the number of paths that sum to a given value.
#The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
#The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
DFS + TwoSum

"""
#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
        
test_tree = TreeNode(3)
test_tree.left = TreeNode(3)
test_tree.right = TreeNode(-4)
test_tree.left.left = TreeNode(5)
test_tree.left.right = TreeNode(6)
test_tree.right.left = TreeNode(7)

#-------------------------------------------------------------------------------
#    Soluton1 - DFS Template Method
#-------------------------------------------------------------------------------
from collections import deque

class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: int
        """
        queue = deque()
        queue.append(([root.val], root, root.val)) # put (curr_path_list, curr_node, sofar_sum) to queue
        ans_list = []
        visited = set()
        ds_size_counter = 0
        while queue:
            ds_size_counter = max(ds_size_counter, len(queue))
            curr_path_list, curr_node, sofar_sum = queue.popleft()
            print(f"Parsing curr_path_list: {curr_path_list}")
            if sofar_sum == target:
                ans_list.append(curr_path_list[:])
            if curr_node.left:
                new_list = curr_path_list[:]
                new_list.append(curr_node.left.val)
                queue.append((new_list, curr_node.left, sofar_sum + curr_node.left.val))
                if curr_node.left not in visited:
                    queue.append(([curr_node.left.val], curr_node.left, curr_node.left.val))
                    visited.add(curr_node.left)
                
            if curr_node.right:
                new_list = curr_path_list[:]
                new_list.append(curr_node.right.val)
                queue.append((new_list, curr_node.right, sofar_sum + curr_node.right.val))
                if curr_node.right not in visited:
                    queue.append(([curr_node.right.val], curr_node.right, curr_node.right.val))
                    visited.add(curr_node.right)
        print(f"size of data structure maximum {ds_size_counter}")
        return ans_list
                         

#-------------------------------------------------------------------------------
#    Solution 2
#-------------------------------------------------------------------------------
    def pathSumBetter(self, root, target):
        # define global result and path
        self.result = 0
        cache = {0:1}
        
        # recursive to get result
        self.dfs(root, target, 0, cache)
        
        # return result
        return self.result
    
    def dfs(self, root, target, currPathSum, cache):
        # exit condition
        if root is None:
            return  
        # calculate currPathSum and required oldPathSum
        currPathSum += root.val
        oldPathSum = currPathSum - target
        # update result and cache
        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1
        
        # dfs breakdown
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)
        # when move to a different branch, the currPathSum is no longer available, hence remove one. 
        cache[currPathSum] -= 1
