# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        # counter to keep track of visited nodes
        self.count = 0
        # variable to store result
        self.result = None
        
        # inorder traversal function
        def inorder(node):
            # base case
            if not node:
                return
            
            # go left
            inorder(node.left)
            
            # visit current node
            self.count += 1
            if self.count == k:  # if kth node is found
                self.result = node.val
                return
            
            # go right
            inorder(node.right)
        
        # start inorder traversal
        inorder(root)
        # return the kth smallest value
        return self.result
