# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        before_dummy = ListNode(0)  
        # Dummy node for list of nodes < x
        after_dummy = ListNode(0)  
        # Dummy node for list of nodes >= x

        before = before_dummy  
        # Pointer to build 'before' list
        after = after_dummy  
        # Pointer to build 'after' list

        while head:
            if head.val < x:
                before.next = head  
                # Add node to 'before' list
                before = before.next  
                # Move before pointer
            else:
                after.next = head  
                # Add node to 'after' list
                after = after.next  
                # Move after pointer
            head = head.next  
            # Move to next node

        after.next = None  
        # End 'after' list to avoid cycle
        before.next = after_dummy.next  
        # Connect 'before' list to 'after' list

        return before_dummy.next  
        # Return new head of partitioned list
