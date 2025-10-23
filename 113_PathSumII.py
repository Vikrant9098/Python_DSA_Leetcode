# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        result = []  # list to store all valid paths
        path = []    # list to store current path

        # Helper function for DFS
        def dfs(node, target):
            if not node:
                return  # base case: null node

            path.append(node.val)  # add current node to path
            target -= node.val     # reduce target by node's value

            # If leaf node and target is 0, add path to result
            if not node.left and not node.right and target == 0:
                result.append(list(path))  # append a copy of current path
            else:
                dfs(node.left, target)   # explore left subtree
                dfs(node.right, target)  # explore right subtree

            path.pop()  # backtrack: remove current node before returning

        dfs(root, targetSum)  # start DFS from root
        return result
