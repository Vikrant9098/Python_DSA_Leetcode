# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []  # list to store inorder traversal
        stack = []  # stack to help traverse iteratively
        current = root  # start from root

        while current or stack:  # iterate while there are nodes to process
            while current:  # go as left as possible
                stack.append(current)  # push current node to stack
                current = current.left  # move to left child

            current = stack.pop()  # pop node from stack
            result.append(current.val)  # visit node

            current = current.right  # move to right child

        return result  # return inorder traversal
