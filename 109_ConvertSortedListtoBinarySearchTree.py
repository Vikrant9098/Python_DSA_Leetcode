# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        # If the linked list is empty, return None (no tree)
        if not head:
            return None

        # If only one node is present, make it a leaf node of BST
        if not head.next:
            return TreeNode(head.val)

        # Initialize pointers
        slow = head       # slow pointer moves one step at a time
        fast = head       # fast pointer moves two steps at a time
        prev = None       # to keep track of node before slow

        # Move slow and fast until fast reaches the end
        while fast and fast.next:
            prev = slow              # store previous node of slow
            slow = slow.next          # move slow one step
            fast = fast.next.next     # move fast two steps

        # Disconnect the left half from middle (split the list)
        if prev:
            prev.next = None

        # slow is now pointing to the middle node (root value)
        root = TreeNode(slow.val)     # create a tree node with middle value

        # Recursively build the left subtree using the left half of list
        root.left = self.sortedListToBST(head)

        # Recursively build the right subtree using the right half of list
        root.right = self.sortedListToBST(slow.next)

        # Return the root node of the constructed BST
        return root
