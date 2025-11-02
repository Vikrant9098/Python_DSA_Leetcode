class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1:
            return 0  # no profit possible with 0 or 1 day

        hold = [0] * n   # profit when holding stock
        sold = [0] * n   # profit when selling stock
        rest = [0] * n   # profit when resting (cooldown)

        hold[0] = -prices[0]  # buy on first day
        sold[0] = 0           # can't sell on first day
        rest[0] = 0           # do nothing on first day

        for i in range(1, n):
            hold[i] = max(hold[i - 1], rest[i - 1] - prices[i])  # keep holding or buy after rest
            sold[i] = hold[i - 1] + prices[i]                    # sell today
            rest[i] = max(rest[i - 1], sold[i - 1])              # stay in rest or cooldown

        return max(sold[-1], rest[-1])  # max profit when not holding stock
