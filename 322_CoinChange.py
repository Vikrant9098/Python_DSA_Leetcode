class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # dp[i] = fewest coins needed to make amount i
        dp = [float('inf')] * (amount + 1)

        # Base case: 0 coins needed for amount 0
        dp[0] = 0

        # Loop through all amounts from 1 to amount
        for i in range(1, amount + 1):
            # Check each coin
            for coin in coins:
                # If coin can be used
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # If not possible to make the amount, return -1
        return -1 if dp[amount] == float('inf') else dp[amount]
