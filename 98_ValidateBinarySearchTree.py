# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # helper function with valid range check
        def helper(node, low, high):
            # if no node, it's valid
            if not node:
                return True
            
            # node value must be within range (low < val < high)
            if not (low < node.val < high):
                return False
            
            # check left and right with updated ranges
            return (helper(node.left, low, node.val) and
                    helper(node.right, node.val, high))
        
        # call helper with full range of values
        return helper(root, float("-inf"), float("inf"))
