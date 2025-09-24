# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if not head or left == right:
            return head  # No need to reverse if list is empty or left == right
        
        # Dummy node to simplify head reversal
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Move prev to the node before the 'left' position
        for _ in range(left - 1):
            prev = prev.next
        
        # start is the first node to reverse
        start = prev.next
        # then is the node that will be moved to the front of the reversed part
        then = start.next
        
        # Reverse the sublist from left to right
        for _ in range(right - left):
            start.next = then.next   # detach 'then'
            then.next = prev.next    # move 'then' to the front
            prev.next = then         # connect prev to 'then'
            then = start.next        # move 'then' to the next node to reverse
        
        # Return new head
        return dummy.next
