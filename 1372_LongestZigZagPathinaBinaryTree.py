# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        self.maxLen = 0  # Initialize a variable to keep track of the maximum ZigZag path length

        def dfs(node, direction, length):
            """
            Recursive DFS function to traverse the tree in ZigZag manner.
            
            :param node: current TreeNode
            :param direction: 0 if we came from left, 1 if from right
            :param length: current ZigZag path length
            """
            if not node:
                return  # If the node is null, there's nothing to do

            # Update the maximum ZigZag length
            self.maxLen = max(self.maxLen, length)

            if direction == 0:
                # Last move was to the left, now go right
                dfs(node.right, 1, length + 1)
                # Restart from left child
                dfs(node.left, 0, 1)
            else:
                # Last move was to the right, now go left
                dfs(node.left, 0, length + 1)
                # Restart from right child
                dfs(node.right, 1, 1)

        # Start DFS from root: try both directions
        dfs(root.left, 0, 1)  # Consider left move first
        dfs(root.right, 1, 1) # Consider right move first

        return self.maxLen  # Return the maximum ZigZag path found
