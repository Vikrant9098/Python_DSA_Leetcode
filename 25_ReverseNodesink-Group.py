# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or k == 1:
            return head  
            # If list is empty or k=1, no reversal needed

        dummy = ListNode(0)  
        # Dummy node before head (helps handle edge cases)
        dummy.next = head  
        # Connect dummy to head
        prev_group_end = dummy  
        # Pointer to track the end of previous group

        while True:
            kth = self.getKthNode(prev_group_end, k)  
            # Find kth node from prev_group_end
            if not kth:
                break  
                # If fewer than k nodes remain, stop

            group_start = prev_group_end.next  
            # First node of current group
            next_group_start = kth.next  
            # Node after kth (start of next group)

            # Reverse current group
            prev, curr = next_group_start, group_start  
            # prev points to next group, curr to current group start
            while curr != next_group_start:
                tmp = curr.next      # Save next node
                curr.next = prev     # Reverse the link
                prev = curr          # Move prev forward
                curr = tmp           # Move curr forward

            prev_group_end.next = kth  
            # Connect previous group to new head (kth)
            prev_group_end = group_start  
            # Move prev_group_end to the end of this group

        return dummy.next  
        # Return new head (after dummy)

    def getKthNode(self, curr, k):
        # Find kth node from current node
        while curr and k > 0:
            curr = curr.next   # Move forward
            k -= 1             # Decrease step count
        return curr            # Return kth node (or None if not enough nodes)
