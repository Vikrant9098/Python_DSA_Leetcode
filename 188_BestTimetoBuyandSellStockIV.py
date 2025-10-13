class Solution(object):  # Define class Solution
    def maxProfit(self, k, prices):  # Define function with k and prices
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)  # Number of days
        if n == 0:  # Check if prices list is empty
            return 0  # Return 0 profit if no prices

        if k >= n // 2:  # If k is large, unlimited transactions possible
            profit = 0  # Initialize profit
            for i in range(1, n):  # Loop from day 1 to end
                if prices[i] > prices[i - 1]:  # If price increased
                    profit += prices[i] - prices[i - 1]  # Add profit
            return profit  # Return total profit

        buy = [float('-inf')] * (k + 1)  # Initialize buy profits
        sell = [0] * (k + 1)  # Initialize sell profits

        for price in prices:  # Loop through each price
            for t in range(1, k + 1):  # Loop through transaction count
                buy[t] = max(buy[t], sell[t - 1] - price)  # Max profit after buying
                sell[t] = max(sell[t], buy[t] + price)  # Max profit after selling

        return sell[k]  # Return max profit after k transactions
