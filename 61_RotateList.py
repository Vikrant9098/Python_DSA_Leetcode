# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k == 0:
            return head  
            # Empty list, single node, or no rotation needed

        tail = head
        length = 1  
        # Initialize tail and length

        while tail.next:
            tail = tail.next  
            # Move to end of list
            length += 1  
            # Count nodes

        tail.next = head  
        # Make the list circular

        k = k % length  
        # Reduce k to avoid extra rotations
        steps_to_new_head = length - k  
        # Steps from old tail to new head

        new_tail = tail
        for _ in range(steps_to_new_head):
            new_tail = new_tail.next  
            # Move to new tail

        new_head = new_tail.next  
        # Next node is new head
        new_tail.next = None  
        # Break the circle to finalize list

        return new_head  
        # Return rotated list head
