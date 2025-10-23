# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []  # if tree is empty, return empty list

        from collections import deque  # import deque for efficient queue operations
        queue = deque([root])  # initialize queue with root node
        result = []  # list to store levels from bottom to top

        while queue:  # loop until queue becomes empty
            level = []  # list to store values of current level
            for _ in range(len(queue)):  # iterate over all nodes at current level
                node = queue.popleft()  # remove front node from queue
                level.append(node.val)  # add its value to the current level list

                if node.left:  # if left child exists
                    queue.append(node.left)  # add left child to queue
                if node.right:  # if right child exists
                    queue.append(node.right)  # add right child to queue

            result.insert(0, level)  # insert current level at the beginning for bottom-up order

        return result  # return the final bottom-up level order list
