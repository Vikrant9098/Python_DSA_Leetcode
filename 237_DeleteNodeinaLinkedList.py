# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # Copy the next node's value into the current node
        node.val = node.next.val
        
        # Skip over the next node to remove it
        node.next = node.next.next
