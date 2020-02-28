# 437. Path Sum III
# Given an array arr of positive integers, consider all binary trees such that:

# Each node has either 0 or 2 children;
# The values of arr correspond to the values of each leaf in an in-order traversal of the tree.  (Recall that a node is a leaf if and only if it has 0 children.)
# The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree respectively.
# Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node.  It is guaranteed this sum fits into a 32-bit integer.#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
DFS + TwoSum

"""

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
