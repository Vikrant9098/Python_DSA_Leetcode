# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)  
        # Dummy node before head (helps handle duplicates at head)
        
        prev = dummy  
        # Pointer to track the last non-duplicate node

        while head:
            if head.next and head.val == head.next.val:
                # Found duplicates (same value repeats)
                while head.next and head.val == head.next.val:
                    head = head.next  
                    # Skip all nodes with this duplicate value
                prev.next = head.next  
                # Connect prev to node after duplicates
            else:
                prev = prev.next  
                # No duplicate, move prev forward
            head = head.next  
            # Move head forward

        return dummy.next  
        # Return new head (after dummy)
