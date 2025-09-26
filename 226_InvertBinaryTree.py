# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # If the tree is empty, return None
        if not root:
            return None

        # Swap left and right child
        root.left, root.right = root.right, root.left

        # Recursively invert left subtree
        self.invertTree(root.left)

        # Recursively invert right subtree
        self.invertTree(root.right)

        # Return the root after inversion
        return root
