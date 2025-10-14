# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_diameter = 0  # store maximum diameter found

        # helper function to compute depth of tree
        def depth(node):
            if not node:
                return 0  # empty node has depth 0

            left = depth(node.left)  # depth of left subtree
            right = depth(node.right)  # depth of right subtree

            # update max diameter at this node
            self.max_diameter = max(self.max_diameter, left + right)

            return 1 + max(left, right)  # return depth of current node

        depth(root)  # start DFS from root
        return self.max_diameter  # return the diameter
