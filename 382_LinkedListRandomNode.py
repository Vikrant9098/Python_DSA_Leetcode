# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random  # used to pick random value

class Solution(object):

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        self.values = []          # store all node values
        while head:               # traverse the linked list
            self.values.append(head.val)  # add each node value
            head = head.next      # move to next node

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.values)  # return random node value


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
