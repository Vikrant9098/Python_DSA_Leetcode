# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val          # value of the current node
#         self.left = left        # pointer to left child
#         self.right = right      # pointer to right child

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        
        if not root:
            return []  # if tree is empty, return empty list

        from collections import deque     # import deque for queue-based BFS
        queue = deque([root])             # initialize queue with root node
        result = []                       # list to store right side view nodes

        while queue:                      # loop until queue becomes empty
            level_size = len(queue)       # number of nodes at current level

            for i in range(level_size):   # iterate through current level
                node = queue.popleft()    # pop the node from queue (FIFO)

                if i == level_size - 1:   # if it's the last node at this level
                    result.append(node.val)  # add its value to result

                if node.left:             # if left child exists
                    queue.append(node.left)  # add left child to queue

                if node.right:            # if right child exists
                    queue.append(node.right) # add right child to queue

        return result                     # return the final right side view list
