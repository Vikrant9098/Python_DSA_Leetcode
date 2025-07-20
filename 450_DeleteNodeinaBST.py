# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val          # value of the current node
#         self.left = left        # pointer to the left child
#         self.right = right      # pointer to the right child

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """

        if not root:
            return None  # base case: if root is null, return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)  # key is in left subtree
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)  # key is in right subtree
        else:
            # node with only one child or no child
            if not root.left:
                return root.right  # return right subtree if left is None
            elif not root.right:
                return root.left   # return left subtree if right is None

            # node with two children: find the inorder successor (smallest in right subtree)
            min_larger_node = self.getMin(root.right)  # get successor
            root.val = min_larger_node.val  # copy successor's value to current node
            root.right = self.deleteNode(root.right, min_larger_node.val)  # delete the successor

        return root  # return updated root

    def getMin(self, node):
        """
        Helper function to find the minimum value node in a subtree.
        """
        while node.left:
            node = node.left  # go to the leftmost node
        return node  # return node with minimum value
