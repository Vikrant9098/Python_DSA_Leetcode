"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)   # store the value of the node
        self.next = next    # pointer to the next node
        self.random = random # pointer to a random node
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # If the original list is empty, return None
        if head is None:
            return None  
        
        # Dictionary to store mapping from original node -> copied node
        node_map = {}
        
        # First pass: create a copy of each node and store in the dictionary
        current = head
        while current:
            node_map[current] = Node(current.val)  # create a new node with the same value
            current = current.next                 # move to the next node in original list
        
        # Second pass: assign next and random pointers for copied nodes
        current = head
        while current:
            copy = node_map[current]                   # get the copied node corresponding to current
            copy.next = node_map.get(current.next)     # set the next pointer of copied node
            copy.random = node_map.get(current.random) # set the random pointer of copied node
            current = current.next                     # move to the next node in original list
        
        # Return the head of the copied linked list
        return node_map[head]
