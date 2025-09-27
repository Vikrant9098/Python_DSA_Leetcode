# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node, curr_sum):
            if not node:
                return 0  # Empty node contributes 0
            
            # Update current sum by appending node's value
            curr_sum = curr_sum * 10 + node.val
            
            # If leaf node, return the current number
            if not node.left and not node.right:
                return curr_sum
            
            # Recurse left and right, return sum
            return dfs(node.left, curr_sum) + dfs(node.right, curr_sum)
        
        # Start DFS with initial sum 0
        return dfs(root, 0)
