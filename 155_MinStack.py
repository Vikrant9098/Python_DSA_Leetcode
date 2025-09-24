class MinStack(object):

    def __init__(self):
        # main stack to store values
        self.stack = []
        # helper stack to track minimums
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        # push value to main stack
        self.stack.append(val)
        # if min_stack empty or val <= last min, push to min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        # pop from main stack
        val = self.stack.pop()
        # if popped value is current min, remove from min_stack too
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        # return last element in stack
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        # return last element in min_stack (current minimum)
        return self.min_stack[-1]
