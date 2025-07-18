# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val          # Node value
#         self.next = next        # Reference to next node

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Base case: if list is empty or has one node, it's already reversed
        if head is None or head.next is None:
            return head

        # Recursively reverse the rest of the list
        new_head = self.reverseList(head.next)

        # Reverse current node's pointer
        head.next.next = head    # Make next node point back to current
        head.next = None         # Break original forward link

        return new_head          # Return new head of the reversed list
