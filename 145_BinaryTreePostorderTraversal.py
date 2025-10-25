# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # Create a list to store the postorder result
        result = []
        
        # If the tree is empty, return an empty list
        if not root:
            return result
        
        # Use two stacks for iterative postorder traversal
        stack1 = [root]  # First stack to process nodes
        stack2 = []      # Second stack to store nodes in reverse order
        
        # Continue until the first stack becomes empty
        while stack1:
            # Pop the top node from stack1
            node = stack1.pop()
            
            # Push the popped node onto stack2
            stack2.append(node)
            
            # If left child exists, push it onto stack1
            if node.left:
                stack1.append(node.left)
            
            # If right child exists, push it onto stack1
            if node.right:
                stack1.append(node.right)
        
        # Pop all nodes from stack2 to get postorder order
        while stack2:
            result.append(stack2.pop().val)
        
        # Return the final postorder traversal list
        return result
