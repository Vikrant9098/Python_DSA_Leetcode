# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val         # Node's value
#         self.left = left       # Reference to left child
#         self.right = right     # Reference to right child

class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # Inner helper function to perform DFS traversal
        def dfs(node, max_so_far):
            if not node:
                return 0  # If node is None (null), return 0 as there are no good nodes here

            # A node is "good" if its value is greater than or equal to all previously seen values on the path
            good = 1 if node.val >= max_so_far else 0

            # Update max_so_far with the maximum value seen so far along this path
            max_so_far = max(max_so_far, node.val)

            # Recurse into the left and right subtree and count the good nodes
            left_good = dfs(node.left, max_so_far)   # Count good nodes in the left subtree
            right_good = dfs(node.right, max_so_far) # Count good nodes in the right subtree

            # Return the total number of good nodes in this subtree
            return good + left_good + right_good

        # Start DFS traversal from root, with root's value as the initial max
        return dfs(root, root.val)
