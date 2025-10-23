# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # Helper function to compute height and check balance
        def checkHeight(node):
            if not node:
                return 0  # height of null node is 0

            leftHeight = checkHeight(node.left)   # recursively get height of left subtree
            if leftHeight == -1:
                return -1  # left subtree not balanced

            rightHeight = checkHeight(node.right)  # recursively get height of right subtree
            if rightHeight == -1:
                return -1  # right subtree not balanced

            if abs(leftHeight - rightHeight) > 1:
                return -1  # current node not balanced

            return max(leftHeight, rightHeight) + 1  # return height of current node

        # If checkHeight returns -1, tree is unbalanced; otherwise, balanced
        return checkHeight(root) != -1
