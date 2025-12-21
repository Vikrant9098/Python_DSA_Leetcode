class Solution(object):                      # Defines the Solution class

    def maxProfit(self, prices, strategy, k):
                                              # Function to calculate maximum profit

        n, h = len(prices), k >> 1              # n = number of days, h = k//2

        base = prev = nxt = best = 0            # Initialize profit-related variables

        for i in range(n):                     # Loop through all days
            base += strategy[i] * prices[i]    # Base profit using original strategy

        for i in range(k):                     # First window of size k
            prev += strategy[i] * prices[i]    # Strategy profit inside window
            if i >= h:                         # Second half of the window
                nxt += prices[i]               # Sum prices for possible modification

        best = max(0, nxt - prev)               # Best improvement from first window

        for r in range(k, n):                  # Slide window from k to n
            l = r - k + 1                      # Left index of current window

            prev += strategy[r] * prices[r]    # Add new right element strategy profit
            prev -= strategy[l - 1] * prices[l - 1]
                                              # Remove left element strategy profit

            nxt += prices[r]                   # Add new price entering modified part
            nxt -= prices[l - 1 + h]           # Remove price leaving modified part

            best = max(best, nxt - prev)       # Update best improvement found

        return base + best                     # Return total maximum profit
944. Delete Columns to Make Sorted