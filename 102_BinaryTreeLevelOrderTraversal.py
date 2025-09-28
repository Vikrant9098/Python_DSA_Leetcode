# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []  # if tree is empty, return empty list

        result = []       # list to store levels
        queue = [root]    # queue for BFS, start with root

        while queue:
            level = []         # list to store current level values
            size = len(queue)  # number of nodes at current level

            for i in range(size):
                node = queue.pop(0)  # remove node from queue
                level.append(node.val)  # add node value to current level list

                # add children to queue for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)  # add current level to result

        return result
