# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        # If tree is empty, no path exists
        if not root:
            return False
        
        # If node is a leaf, check if remaining sum equals node value
        if not root.left and not root.right:
            return targetSum == root.val
        
        # Subtract current node's value from target and check left/right
        remaining = targetSum - root.val
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)
