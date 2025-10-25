# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # If the list has 0 or 1 node, no need to reorder
        if not head or not head.next:
            return

        # Step 1: Find the middle of the linked list using slow and fast pointers
        slow, fast = head, head  # Initialize both pointers at the head
        while fast and fast.next:  # Move fast by 2 and slow by 1 until fast reaches the end
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list
        prev, curr = None, slow.next  # Start reversing from the node after the middle
        slow.next = None  # Break the list into two halves
        while curr:  # Continue until current becomes None
            next_temp = curr.next  # Store next node temporarily
            curr.next = prev  # Reverse the link
            prev = curr  # Move prev one step forward
            curr = next_temp  # Move curr one step forward

        # Step 3: Merge the two halves alternately
        first, second = head, prev  # Pointers to both halves
        while second:  # Continue until second half is exhausted
            temp1 = first.next  # Store next node of first half
            temp2 = second.next  # Store next node of second half

            first.next = second  # Link first node to one from second half
            second.next = temp1  # Link that node to next in first half

            first = temp1  # Move first pointer ahead
            second = temp2  # Move second pointer ahead
