# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        # Map from value to index in inorder for quick lookup
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        # Index pointer for postorder (start from last element)
        self.post_index = len(postorder) - 1

        # Recursive helper function
        def helper(left, right):
            # If no elements to construct the tree
            if left > right:
                return None

            # Pick current root from postorder
            root_val = postorder[self.post_index]
            self.post_index -= 1
            root = TreeNode(root_val)

            # Find index of root in inorder
            index = inorder_map[root_val]

            # Important: build right subtree first
            root.right = helper(index + 1, right)
            root.left = helper(left, index - 1)

            return root

        return helper(0, len(inorder) - 1)
