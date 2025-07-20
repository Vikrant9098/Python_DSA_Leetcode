# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val          # value of the node
#         self.left = left        # pointer to the left child
#         self.right = right      # pointer to the right child

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        from collections import deque           # import deque for efficient queue operations
        queue = deque([root])                   # initialize queue with root node

        max_sum = float('-inf')                 # store the maximum level sum found so far
        max_level = 1                           # store the level number of max_sum
        current_level = 1                       # level counter, root is at level 1

        while queue:                            # continue until queue is empty
            level_size = len(queue)             # number of nodes in the current level
            level_sum = 0                       # sum of node values at this level

            for _ in range(level_size):         # iterate through all nodes in the level
                node = queue.popleft()          # dequeue the current node
                level_sum += node.val           # add node's value to current level sum

                if node.left:                   # if left child exists
                    queue.append(node.left)     # add left child to queue
                if node.right:                  # if right child exists
                    queue.append(node.right)    # add right child to queue

            if level_sum > max_sum:             # if current level's sum is the highest so far
                max_sum = level_sum             # update max_sum
                max_level = current_level       # update corresponding level number

            current_level += 1                  # move to the next level

        return max_level                        # return the level with the maximum sum
