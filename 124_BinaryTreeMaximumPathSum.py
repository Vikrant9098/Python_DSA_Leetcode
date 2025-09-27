# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_sum = float('-inf')  # To store the maximum path sum

        def dfs(node):
            if not node:
                return 0  # Base case: null node contributes 0
            
            # Max path sum from left and right (ignore negative paths)
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            
            # Update global maximum including current node
            self.max_sum = max(self.max_sum, node.val + left + right)
            
            # Return max sum extending to parent (only one side can be chosen)
            return node.val + max(left, right)
        
        dfs(root)  # Start DFS
        return self.max_sum
