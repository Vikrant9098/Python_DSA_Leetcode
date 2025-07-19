# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val         # Value of the current node
#         self.left = left       # Left child
#         self.right = right     # Right child

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """

        # Dictionary to store prefix sums and their frequencies
        prefix_sums = {0: 1}  # There is one path that sums to 0 (empty path)

        def dfs(node, curr_sum):
            if not node:
                return 0  # No path if node is None

            # Add current node's value to cumulative sum
            curr_sum += node.val

            # Number of valid paths ending at this node = number of times (curr_sum - targetSum) occurred before
            num_paths = prefix_sums.get(curr_sum - targetSum, 0)

            # Update prefix_sums with the current cumulative sum
            prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1

            # Recurse on left and right children to continue the path
            num_paths += dfs(node.left, curr_sum)
            num_paths += dfs(node.right, curr_sum)

            # After visiting children, backtrack: remove the current sum count (important for other paths)
            prefix_sums[curr_sum] -= 1

            # Return total number of valid paths found in this subtree
            return num_paths

        # Start DFS from the root with initial cumulative sum = 0
        return dfs(root, 0)
