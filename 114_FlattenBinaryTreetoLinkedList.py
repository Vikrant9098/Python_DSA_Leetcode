# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        curr = root  # Start from the root node
        
        # Loop until all nodes are processed
        while curr:
            if curr.left:
                # Find the rightmost node of the left subtree
                prev = curr.left
                while prev.right:
                    prev = prev.right
                
                # Connect current right subtree to the rightmost node
                prev.right = curr.right
                
                # Move left subtree to right
                curr.right = curr.left
                curr.left = None  # Set left to None
            
            # Move to the next node (always goes right now)
            curr = curr.right
