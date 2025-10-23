# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # If tree is empty, return 0
        if not root:
            return 0

        # If left child is None, minimum depth is 1 + depth of right subtree
        if not root.left:
            return self.minDepth(root.right) + 1

        # If right child is None, minimum depth is 1 + depth of left subtree
        if not root.right:
            return self.minDepth(root.left) + 1

        # If both children exist, return 1 + min(depth of left, depth of right)
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
