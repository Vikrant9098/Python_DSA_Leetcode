# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Create two pointers for cycle detection
        slow = head
        fast = head

        # Move pointers to detect if a cycle exists
        while fast and fast.next:
            slow = slow.next          # move slow one step
            fast = fast.next.next     # move fast two steps

            # If they meet, cycle detected
            if slow == fast:
                break

        # If fast reached the end, no cycle
        else:
            return None

        # Move slow to head to find the cycle start
        slow = head

        # Move both one step until they meet
        while slow != fast:
            slow = slow.next
            fast = fast.next

        # Meeting point is the start of the cycle
        return slow
