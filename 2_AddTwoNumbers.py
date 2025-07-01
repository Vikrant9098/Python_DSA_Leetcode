class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy head to simplify list construction
        dummy_head = ListNode(0)
        # Current pointer to build the result list
        current = dummy_head
        # Initialize carry to handle sums >= 10
        carry = 0
        
        # Continue while there are digits in either list or carry exists
        while l1 or l2 or carry:
            # Get the current digit from l1 (0 if l1 is None)
            val1 = l1.val if l1 else 0
            # Get the current digit from l2 (0 if l2 is None)
            val2 = l2.val if l2 else 0
            
            # Calculate the sum of current digits plus carry
            total = val1 + val2 + carry
            # Extract the digit to store (remainder when divided by 10)
            digit = total % 10
            # Calculate new carry (quotient when divided by 10)
            carry = total // 10
            
            # Create new node with the calculated digit
            current.next = ListNode(digit)
            # Move current pointer to the new node
            current = current.next
            
            # Move to next nodes if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # Return the actual result (skip dummy head)
        return dummy_head.next
