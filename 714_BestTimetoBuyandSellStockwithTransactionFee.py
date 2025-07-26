class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """

        n = len(prices)

        # hold: max profit when holding a stock
        # cash: max profit when not holding a stock
        hold = -prices[0]  # buy at day 0
        cash = 0           # no stock, profit is 0

        for i in range(1, n):
            # either keep cash or sell stock today
            cash = max(cash, hold + prices[i] - fee)

            # either keep holding or buy today
            hold = max(hold, cash - prices[i])

        # final profit must be without holding stock
        return cash
