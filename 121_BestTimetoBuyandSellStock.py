class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')   # Keep track of the minimum price so far
        max_profit = 0             # Keep track of the maximum profit so far

        for price in prices:
            # Update the minimum price if we find a smaller one
            if price < min_price:
                min_price = price
            # Calculate profit if sold today, update max_profit if higher
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
