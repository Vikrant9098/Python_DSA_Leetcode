# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        # Create a dummy node before the head
        dummy = ListNode(0)
        
        # Link dummy to the head
        dummy.next = head

        # Start with dummy node
        current = dummy

        # Loop through the list
        while current.next:
            # If next node has the value to remove
            if current.next.val == val:
                # Skip that node
                current.next = current.next.next
            else:
                # Move to next node
                current = current.next

        # Return new head after dummy
        return dummy.next
