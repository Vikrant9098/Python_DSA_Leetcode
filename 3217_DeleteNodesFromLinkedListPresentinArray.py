# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Convert nums to a set for O(1) lookup
        to_delete = set(nums)
        
        # Create a dummy node to handle deletions at the head
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize previous and current pointers
        prev, curr = dummy, head
        
        # Traverse the linked list
        while curr:
            if curr.val in to_delete:
                # Skip current node if value should be deleted
                prev.next = curr.next
            else:
                # Move prev forward only if node is kept
                prev = curr
            curr = curr.next
        
        # Return modified list starting from dummy.next
        return dummy.next
