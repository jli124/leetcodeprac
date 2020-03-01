#938 Range Sum of BST
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Recursive

"""

#-------------------------------------------------------------------------------
#    Soluton1 --- Recursive
#-------------------------------------------------------------------------------
## recursive
class Solution(object):
    def rangSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                if L < node.val:
                    dfs(node.left)
                if node.val < R:
                    dfs(node.right)
        self.ans = 0
        dfs(root)
        return self.ans

#-------------------------------------------------------------------------------
#    Soluton2 ---Iterative
#-------------------------------------------------------------------------------
class Solution(object):
    def rangSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if L <= node.val <= R:
                    ans += node.val
                if L < node.val:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
        return ans
