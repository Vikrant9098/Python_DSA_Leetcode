# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # Helper function to check if two trees are mirrors
        def isMirror(t1, t2):
            # If both nodes are None, they are mirrors
            if not t1 and not t2:
                return True
            # If only one is None, not mirrors
            if not t1 or not t2:
                return False
            # Values must be equal, and children must be mirror
            return (t1.val == t2.val and 
                    isMirror(t1.left, t2.right) and 
                    isMirror(t1.right, t2.left))

        # An empty tree is symmetric
        if not root:
            return True
        return isMirror(root.left, root.right)
