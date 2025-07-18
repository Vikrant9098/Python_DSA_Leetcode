# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # Base case: If the node is None (empty subtree), depth is 0
        if not root:
            return 0

        # Recursively calculate the depth of the left subtree
        left_depth = self.maxDepth(root.left)

        # Recursively calculate the depth of the right subtree
        right_depth = self.maxDepth(root.right)

        # Return 1 + max depth of left and right subtree
        return 1 + max(left_depth, right_depth)
