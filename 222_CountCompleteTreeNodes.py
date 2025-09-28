# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)

        # If left and right subtree heights are equal, left subtree is perfect
        if left_height == right_height:
            # (1 << left_height) gives 2^left_height
            return (1 << left_height) + self.countNodes(root.right)
        else:
            # Otherwise, right subtree is perfect
            return (1 << right_height) + self.countNodes(root.left)

    def getHeight(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height
