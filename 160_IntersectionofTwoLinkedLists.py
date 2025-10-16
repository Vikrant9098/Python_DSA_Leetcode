# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        # If either list is empty, return None
        if not headA or not headB:
            return None

        # Initialize two pointers at the heads of the lists
        a, b = headA, headB

        # Move pointers until they meet or both reach None
        while a != b:
            # Move to next node, or switch to the other list's head if at the end
            a = a.next if a else headB
            b = b.next if b else headA

        # Either intersection node or None
        return a
