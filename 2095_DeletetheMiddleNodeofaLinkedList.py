# Definition for singly-linked list.
# Each node in the list has a value and a reference to the next node.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val          # Initialize the node's value
        self.next = next        # Pointer to the next node in the list

class Solution(object):
    def deleteMiddle(self, head):
        """
        Deletes the middle node from a singly linked list and returns the modified list.
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # Edge case: If the list has only one node, deleting the middle means returning None.
        if not head or not head.next:
            return None

        # Initialize slow and fast pointers. Slow will move one step at a time, fast moves two.
        slow = head
        fast = head
        prev = None  # This keeps track of the node before the slow pointer

        # Traverse the list to find the middle node using the two-pointer technique
        while fast and fast.next:
            prev = slow            # Store the previous node of 'slow'
            slow = slow.next       # Move 'slow' by one step
            fast = fast.next.next  # Move 'fast' by two steps

        # Now 'slow' is pointing to the middle node. We skip it by linking 'prev' to 'slow.next'
        prev.next = slow.next

        # Return the head of the modified linked list
        return head
