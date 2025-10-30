# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        result = []  # List to store all root-to-leaf paths
        
        def dfs(node, path):
            if not node:  # If the node is None, return
                return
            if not node.left and not node.right:
                # If it's a leaf node, add the path + current node value to result
                result.append(path + str(node.val))
                return
            # Continue DFS on left child with updated path
            dfs(node.left, path + str(node.val) + "->")
            # Continue DFS on right child with updated path
            dfs(node.right, path + str(node.val) + "->")
        
        dfs(root, "")  # Start DFS traversal from root
        return result  # Return all collected paths
