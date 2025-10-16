# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):  # define Solution class
    def isPalindrome(self, head):  # define method to check palindrome
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head or not head.next:  # if list is empty or has 1 node
            return True  # it's a palindrome

        # Step 1: Find the middle of the list
        slow = fast = head  # initialize slow and fast pointers
        while fast.next and fast.next.next:  # loop until fast reaches end
            slow = slow.next  # move slow one step
            fast = fast.next.next  # move fast two steps

        # Step 2: Reverse the second half
        second_half = self.reverse(slow.next)  # reverse nodes after middle

        # Step 3: Compare first half and second half
        first_half = head  # pointer for first half
        second_ptr = second_half  # pointer for reversed second half
        palindrome = True  # assume it's a palindrome
        while palindrome and second_ptr:  # loop until mismatch or end
            if first_half.val != second_ptr.val:  # if values differ
                palindrome = False  # not a palindrome
            first_half = first_half.next  # move first half pointer
            second_ptr = second_ptr.next  # move second half pointer

        # Step 4 (optional): Restore the list
        slow.next = self.reverse(second_half)  # reverse second half back

        return palindrome  # return result

    # Helper function to reverse a linked list
    def reverse(self, head):  # define reverse function
        prev = None  # previous node
        curr = head  # current node
        while curr:  # while not end
            next_temp = curr.next  # store next node
            curr.next = prev  # reverse link
            prev = curr  # move prev forward
            curr = next_temp  # move curr forward
        return prev  # return new head
