# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val          # value of the current node
#         self.left = left        # pointer to the left child
#         self.right = right      # pointer to the right child

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """

        if not root:
            return None  # if current node is null, return None (val not found)

        if root.val == val:
            return root  # if current node's value matches target, return this node

        if val < root.val:
            return self.searchBST(root.left, val)  # search in left subtree if val is smaller

        else:
            return self.searchBST(root.right, val) # search in right subtree if val is greater
