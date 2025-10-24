# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        # Store the node value
        self.val = val
        # Pointer to left child
        self.left = left
        # Pointer to right child
        self.right = right
        # Pointer to next right node
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # If tree is empty, return None
        if not root:
            return None

        # Start from the leftmost node of the first level (root)
        leftmost = root

        # Keep going until we reach the last level (no left child)
        while leftmost.left:
            # Start with the first node on the current level
            head = leftmost

            # Traverse all nodes in the current level
            while head:
                # Connect the left child to the right child
                head.left.next = head.right

                # If there is a next node, connect right child to next node's left child
                if head.next:
                    head.right.next = head.next.left

                # Move to the next node in the same level
                head = head.next

            # Move down to the next level (go to the leftmost child)
            leftmost = leftmost.left

        # Return the root node (tree with connected next pointers)
        return root
