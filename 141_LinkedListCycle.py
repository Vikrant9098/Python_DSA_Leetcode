# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # If list is empty or has only one node, no cycle
        if head is None or head.next is None:
            return False
        
        # Initialize two pointers
        slow = head       # moves 1 step at a time
        fast = head.next  # moves 2 steps at a time
        
        # Traverse the list
        while slow != fast:
            # If fast reaches end, no cycle
            if fast is None or fast.next is None:
                return False
            # Move slow by 1
            slow = slow.next
            # Move fast by 2
            fast = fast.next.next
        
        # If slow == fast, cycle exists
        return True
