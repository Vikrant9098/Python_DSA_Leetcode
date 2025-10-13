class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # If no prices, profit is 0
        if not prices:
            return 0

        buy1 = float('inf')   # Minimum price for first buy
        profit1 = 0           # Max profit after first sell
        buy2 = float('inf')   # Effective price for second buy
        profit2 = 0           # Max profit after second sell

        # Loop through each price
        for price in prices:
            buy1 = min(buy1, price)               # Find lowest first buy price
            profit1 = max(profit1, price - buy1)  # Best profit after first sell
            buy2 = min(buy2, price - profit1)     # Effective second buy cost
            profit2 = max(profit2, price - buy2)  # Best profit after second sell

        return profit2  # Return total max profit after at most two transactions
