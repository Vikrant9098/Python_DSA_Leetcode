# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.stack = []
        self._pushLeft(root)  # Initialize with the leftmost path

    def next(self):
        """
        :rtype: int
        """
        # Pop the smallest node from the stack
        node = self.stack.pop()
        # If the node has a right child, push its leftmost path
        if node.right:
            self._pushLeft(node.right)
        return node.val

    def hasNext(self):
        """
        :rtype: bool
        """
        # If stack is not empty, there is a next element
        return len(self.stack) > 0

    def _pushLeft(self, node):
        # Push all left nodes onto the stack
        while node:
            self.stack.append(node)
            node = node.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
