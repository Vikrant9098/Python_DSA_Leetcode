# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        # If tree is empty, return empty list
        if not root:
            return []

        result = []           # list to store averages
        queue = [root]        # queue for BFS, start with root

        # Process each level of the tree
        while queue:
            level_sum = 0     # sum of values at this level
            size = len(queue) # number of nodes at this level

            # Process all nodes in the current level
            for i in range(size):
                node = queue.pop(0)  # take one node from the queue
                level_sum += node.val  # add node value to sum

                # if left child exists, add to queue
                if node.left:
                    queue.append(node.left)
                # if right child exists, add to queue
                if node.right:
                    queue.append(node.right)

            # compute average and add to result list
            result.append(level_sum * 1.0 / size)

        # return list of averages for all levels
        return result
