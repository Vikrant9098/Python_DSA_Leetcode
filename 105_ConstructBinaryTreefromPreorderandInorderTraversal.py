# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        # Map to store value -> index for inorder array for quick lookup
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        # Index pointer for preorder array
        self.preorder_index = 0

        # Recursive function to build the tree
        def arrayToTree(left, right):
            # Base case: if no elements are available to construct the tree
            if left > right:
                return None

            # Select the current element as the root from preorder
            root_val = preorder[self.preorder_index]
            self.preorder_index += 1

            # Create the root node
            root = TreeNode(root_val)

            # Build left and right subtrees
            # Elements left of root_val in inorder are in the left subtree
            # Elements right of root_val in inorder are in the right subtree
            root.left = arrayToTree(left, inorder_map[root_val] - 1)
            root.right = arrayToTree(inorder_map[root_val] + 1, right)

            return root

        # Build the tree using full inorder range
        return arrayToTree(0, len(inorder) - 1)
