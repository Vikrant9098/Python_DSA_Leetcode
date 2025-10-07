# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # if list is empty or has only one node, return as it is already sorted
        if not head or not head.next:
            return head
        
        # find the middle node of the list
        mid = self.getMiddle(head)
        
        # store the head of right half
        right = mid.next
        
        # break the list into two halves
        mid.next = None
        
        # recursively sort the left half
        left_sorted = self.sortList(head)
        
        # recursively sort the right half
        right_sorted = self.sortList(right)
        
        # merge the two sorted halves
        return self.merge(left_sorted, right_sorted)
    
    # helper function to find middle node using slow-fast pointers
    def getMiddle(self, head):
        # slow and fast pointers start from head
        slow, fast = head, head.next
        
        # move slow by 1 and fast by 2 until fast reaches end
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow will be at the middle node
        return slow
    
    # helper function to merge two sorted linked lists
    def merge(self, l1, l2):
        # create a dummy node to start the merged list
        dummy = ListNode(0)
        tail = dummy  # tail will track the last node of merged list
        
        # merge while both lists have nodes
        while l1 and l2:
            # choose the smaller value node
            if l1.val < l2.val:
                tail.next = l1   # attach l1 node to merged list
                l1 = l1.next     # move l1 pointer
            else:
                tail.next = l2   # attach l2 node to merged list
                l2 = l2.next     # move l2 pointer
            tail = tail.next     # move tail to next node
        
        # connect remaining nodes from l1 or l2
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        
        # return the sorted merged list starting from dummy.next
        return dummy.next
