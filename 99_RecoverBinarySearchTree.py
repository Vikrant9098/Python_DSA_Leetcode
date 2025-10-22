# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        first = second = prev = None  # Nodes to swap and previous node
        curr = root  # Start from root

        while curr:  # Traverse tree
            if not curr.left:  # No left child
                if prev and prev.val > curr.val:  # Check violation
                    if not first: first = prev  # First swapped node
                    second = curr  # Second swapped node
                prev = curr  # Update previous
                curr = curr.right  # Move right
            else:
                pre = curr.left  # Find predecessor
                while pre.right and pre.right != curr:  # Go to rightmost
                    pre = pre.right

                if not pre.right:  # Thread not created
                    pre.right = curr  # Create thread
                    curr = curr.left  # Move left
                else:  # Thread exists
                    pre.right = None  # Remove thread
                    if prev and prev.val > curr.val:  # Check violation
                        if not first: first = prev  # First swapped node
                        second = curr  # Second swapped node
                    prev = curr  # Update previous
                    curr = curr.right  # Move right

        first.val, second.val = second.val, first.val  # Swap the two nodes to fix BST
