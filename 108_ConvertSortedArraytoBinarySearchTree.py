# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """

        # Helper function to build BST from nums[left...right]
        def buildBST(left, right):
            if left > right:  # Base case: no elements to process
                return None

            mid = left + (right - left) // 2  # Middle element as root
            root = TreeNode(nums[mid])        # Create root node

            # Recursively build left and right subtrees
            root.left = buildBST(left, mid - 1)
            root.right = buildBST(mid + 1, right)

            return root  # Return the constructed subtree

        return buildBST(0, len(nums) - 1)  # Start recursion with full array
