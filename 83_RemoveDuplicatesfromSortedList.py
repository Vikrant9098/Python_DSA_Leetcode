# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # If list is empty or has only one node, return it
        if not head or not head.next:
            return head

        # Start from the first node
        current = head

        # Traverse the list
        while current and current.next:
            # If current and next node values are same
            if current.val == current.next.val:
                # Skip the next node (remove duplicate)
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next

        # Return the head of the updated list
        return head
