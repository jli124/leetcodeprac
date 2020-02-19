#101. Symmetric Tree
#Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Recursive

"""

#-------------------------------------------------------------------------------
#    Soluton1 ---Recursive, D&C
#-------------------------------------------------------------------------------
## recursive
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        def node_sym(node1, node2):
            if not node1 and not node2: return True
            if not node1 or not node2 or node1.val != node2.val: return False
            else:
                left = node_sym(node1.left, node2.right)
                right = node_sym(node1.right,node2.left)
                return left and right
        
        return node_sym(root,root)
#-------------------------------------------------------------------------------
#    Soluton2 ---Iterative, preorder traversal
#-------------------------------------------------------------------------------
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        stack = [(root, root)]
        while stack:
            l, r = stack.pop()
            
            if not l and not r:
                continue
            elif not l or not r or l.val != r.val:
                return False
            
            stack.append((l.left, r.right))
            stack.append((l.right, r.left))
            
        return True
#-------------------------------------------------------------------------------
#    Soluton3 ---BFS
#-------------------------------------------------------------------------------
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        queue, temp = [root], []
        
        # BFS
        while queue:
            # two pointers, one from the beginning, one from the back
            l, r = 0, len(queue) - 1
            
            while l < r:
                node1, node2 = queue[l], queue[r]
                l += 1
                r -= 1
                
                if not node1 and not node2:
                    continue
                elif not node1 or not node2 or node1.val != node2.val:
                    return False
              
            for node in queue:
                if not node:
                    continue
                
                temp.append(node.left)
                temp.append(node.right)
            
            queue, temp = temp, []
        
        return True  