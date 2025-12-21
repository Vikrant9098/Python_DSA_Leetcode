def maximumProfit(self, A: List[int], k: int) -> int:
    
    bought = [-inf] * k          # Max profit after buying (k states)
    res = [0] * (k + 1)          # Max profit with j transactions completed
    sold = [0] * k               # Max profit after selling (k states)

    # Loop through each day's price
    for a in A:

        # Loop transactions in reverse to avoid overwrite
        for j in range(k, 0, -1):

            # Update best profit for j transactions
            res[j] = max(
                res[j],                  # Do nothing
                bought[j - 1] + a,        # Sell previously bought stock
                sold[j - 1] - a           # Buy after previous sell
            )

            # Update buy state
            bought[j - 1] = max(
                bought[j - 1],            # Keep previous buy
                res[j - 1] - a             # Buy at current price
            )

            # Update sell state
            sold[j - 1] = max(
                sold[j - 1],              # Keep previous sell
                res[j - 1] + a             # Sell at current price
            )

    return max(res)               # Return maximum profit
