# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # variable to track previous node value
        self.prev = None
        # variable to store minimum difference
        self.minDiff = float('inf')
        
        # inorder traversal function
        def inorder(node):
            # base case: if node is None, return
            if not node:
                return
            
            # go left first
            inorder(node.left)
            
            # if we have a previous value, update minDiff
            if self.prev is not None:
                self.minDiff = min(self.minDiff, node.val - self.prev)
            
            # update previous to current node value
            self.prev = node.val
            
            # go right next
            inorder(node.right)
        
        # call inorder on root
        inorder(root)
        # return the minimum difference
        return self.minDiff
