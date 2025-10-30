# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Traverse the tree starting from the root
        while root:
            # If both p and q are smaller than root, move to the left subtree
            if p.val < root.val and q.val < root.val:
                root = root.left
            # If both p and q are greater than root, move to the right subtree
            elif p.val > root.val and q.val > root.val:
                root = root.right
            # Otherwise, we found the split point — this node is the LCA
            else:
                return root
