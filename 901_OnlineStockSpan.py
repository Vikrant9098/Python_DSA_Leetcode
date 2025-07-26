class StockSpanner(object):

    def __init__(self):
        # Initialize a stack to store pairs of (price, span)
        self.stack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        span = 1  # Initialize the span for the current price as 1

        # While the stack is not empty and the price at the top of the stack is less than or equal to current price
        while self.stack and self.stack[-1][0] <= price:
            # Add the span of the top element to the current span
            span += self.stack.pop()[1]

        # Push the current price and its span to the stack
        self.stack.append((price, span))

        # Return the span
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
