# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """

        # Helper function to collect leaf values of a tree
        def getLeaves(root):
            # List to store leaf values
            leaves = []

            # Define a recursive DFS function
            def dfs(node):
                if not node:
                    return
                # If it's a leaf node, append its value
                if not node.left and not node.right:
                    leaves.append(node.val)
                # Continue DFS on left and right child
                dfs(node.left)
                dfs(node.right)

            dfs(root)
            return leaves

        # Get leaf sequences for both trees
        leaves1 = getLeaves(root1)
        leaves2 = getLeaves(root2)

        # Compare both leaf sequences
        return leaves1 == leaves2

        # Time Complexity: O(n)
        # Space Complexity: O(n)