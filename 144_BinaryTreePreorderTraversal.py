# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # Create a list to store preorder traversal result
        result = []
        
        # If root is None, return empty list
        if not root:
            return result
        
        # Create a stack to help with iterative traversal
        stack = [root]
        
        # Continue until stack becomes empty
        while stack:
            # Pop the top node from stack
            node = stack.pop()
            
            # Add the node's value to the result list
            result.append(node.val)
            
            # If right child exists, push it first
            if node.right:
                stack.append(node.right)
            
            # If left child exists, push it next
            if node.left:
                stack.append(node.left)
        
        # Return the final preorder traversal list
        return result
