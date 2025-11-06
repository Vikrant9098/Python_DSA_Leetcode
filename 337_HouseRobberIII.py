# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        # call helper to get [notRob, rob] for root
        res = self.dfs(root)
        # return max of robbing or not robbing root
        return max(res[0], res[1])

    def dfs(self, node):
        # if node is None, return [0, 0]
        if not node:
            return [0, 0]

        # get values from left and right child
        left = self.dfs(node.left)
        right = self.dfs(node.right)

        # if rob this node, can't rob its children
        rob = node.val + left[0] + right[0]

        # if not rob this node, take max from each child
        notRob = max(left[0], left[1]) + max(right[0], right[1])

        # return [notRob, rob]
        return [notRob, rob]
