# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # Edge case: if list is empty or has only one node, return it directly
        if not head or not head.next:
            return head

        # Initialize pointers for odd and even
        odd = head                      # Start of odd-indexed nodes
        even = head.next               # Start of even-indexed nodes
        even_head = even               # Store start of even list to attach later

        # Traverse while there are even nodes and next odd nodes
        while even and even.next:
            odd.next = even.next       # Connect current odd to the next odd node
            odd = odd.next             # Move odd pointer forward

            even.next = odd.next       # Connect current even to the next even node
            even = even.next           # Move even pointer forward

        # Attach the even list after odd list
        odd.next = even_head

        # Return the reordered head
        return head
