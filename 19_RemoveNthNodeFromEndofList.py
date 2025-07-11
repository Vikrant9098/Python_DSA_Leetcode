# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Create a dummy node to handle edge cases (like removing the first node)
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize two pointers both starting at dummy
        first = dummy
        second = dummy
        
        # Move first pointer n+1 steps ahead to create gap of n nodes
        for i in range(n + 1):
            first = first.next
        
        # Move both pointers until first reaches the end
        # This ensures second pointer is at the node before the target node
        while first is not None:
            first = first.next
            second = second.next
        
        # Remove the nth node from end by skipping it
        second.next = second.next.next
        
        # Return the head of modified list (dummy.next)
        return dummy.next