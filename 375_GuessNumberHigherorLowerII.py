class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[i][j] = minimum money needed to guarantee a win between numbers i and j
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        # loop for all possible range lengths (from 2 to n)
        for length in range(2, n + 1):
            # start of range
            for start in range(1, n - length + 2):
                end = start + length - 1  # end of range
                dp[start][end] = float('inf')  # set to a large value first

                # try every possible guess x in the range [start, end)
                for x in range(start, end):
                    # cost = money paid for guessing x + worst side cost
                    cost = x + max(dp[start][x - 1], dp[x + 1][end])
                    # keep the smallest cost
                    dp[start][end] = min(dp[start][end], cost)

        # answer for range [1, n]
        return dp[1][n]
