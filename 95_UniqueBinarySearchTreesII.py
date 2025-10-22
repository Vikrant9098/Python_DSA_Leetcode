# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """
        if n == 0:  # If no nodes
            return []  # Return empty list

        def build(start, end):  # Helper function to build trees
            res = []  # List to store all possible trees
            if start > end:  # If range invalid
                res.append(None)  # Add None as empty subtree
                return res

            for i in range(start, end + 1):  # Choose each number as root
                left = build(start, i - 1)  # All possible left subtrees
                right = build(i + 1, end)  # All possible right subtrees

                for l in left:  # Combine left subtree
                    for r in right:  # With each right subtree
                        root = TreeNode(i)  # Create root node
                        root.left = l  # Attach left subtree
                        root.right = r  # Attach right subtree
                        res.append(root)  # Add complete tree to result
            return res  # Return all trees for this range

        return build(1, n)  # Build all trees using values from 1 to n
