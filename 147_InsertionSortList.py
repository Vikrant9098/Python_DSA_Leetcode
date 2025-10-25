# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to simplify insertions at head
        dummy = ListNode(0)
        
        # Pointer to traverse the original list
        curr = head
        
        # Traverse all nodes in the original list
        while curr:
            # Start from dummy to find insertion point
            prev = dummy
            
            # Find the correct position to insert current node
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            
            # Store next node before changing links
            next_temp = curr.next
            
            # Insert current node in sorted position
            curr.next = prev.next
            prev.next = curr
            
            # Move to next node in original list
            curr = next_temp
        
        # Return the sorted list starting after dummy
        return dummy.next
