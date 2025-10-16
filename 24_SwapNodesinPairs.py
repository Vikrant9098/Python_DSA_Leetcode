# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node before head to simplify swapping
        dummy = ListNode(0)
        dummy.next = head

        # prev points to node before the pair being swapped
        prev = dummy

        # Loop while there are at least two nodes left
        while head and head.next:
            # Identify two nodes to be swapped
            first = head
            second = head.next

            # Perform the swap
            prev.next = second        # Link previous node to second
            first.next = second.next  # First node points to node after second
            second.next = first       # Second node points to first

            # Move pointers ahead for next swap
            prev = first
            head = first.next

        # Return the new head (dummy.next points to new list)
        return dummy.next
