# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []  # if tree is empty, return empty list

        result = []            # list to store final zigzag order
        queue = [root]         # queue for BFS
        left_to_right = True    # flag to alternate direction

        while queue:
            level = []          # list to store current level
            size = len(queue)   # number of nodes at current level

            for i in range(size):
                node = queue.pop(0)  # remove node from queue

                # add value according to current direction
                if left_to_right:
                    level.append(node.val)      # left to right
                else:
                    level.insert(0, node.val)  # right to left

                # add children to queue for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)         # add current level to result
            left_to_right = not left_to_right  # flip direction for next level

        return result
