# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # Start from the root node
        head = root
        
        # Loop until no more levels
        while head:
            # Dummy node for the next level
            dummy = Node(0)
            # Tail pointer to build links
            tail = dummy
            
            # Traverse the current level
            while head:
                # If left child exists, connect it
                if head.left:
                    tail.next = head.left
                    tail = tail.next
                # If right child exists, connect it
                if head.right:
                    tail.next = head.right
                    tail = tail.next
                # Move to next node in current level
                head = head.next
            
            # Move down to the first node of the next level
            head = dummy.next
        
        # Return updated root
        return root
