class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        nodes = preorder.split(",")  # split the input string by commas
        slots = 1  # start with one slot for the root node

        # go through each node
        for node in nodes:
            slots -= 1  # each node uses one slot
            if slots < 0:  # if no slot left, invalid
                return False

            if node != "#":  # if node is not null
                slots += 2  # add two new slots for its children

        return slots == 0  # valid if all slots are exactly used
