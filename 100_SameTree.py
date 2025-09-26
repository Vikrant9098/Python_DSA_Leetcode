# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        # If both nodes are None, they are the same
        if not p and not q:
            return True

        # If one is None and the other is not, not the same
        if not p or not q:
            return False

        # If values are different, not the same
        if p.val != q.val:
            return False

        # Recursively check left subtree and right subtree
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
