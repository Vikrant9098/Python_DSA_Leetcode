class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """

        MOD = 10**9 + 7  # Since the result can be very large, we use modulo to keep it within limits.

        # Base case: Only 1 column, only 1 way to place a vertical domino.
        if n == 1:
            return 1

        # Base case: 2 columns — either two vertical dominoes or two horizontal ones => 2 ways.
        if n == 2:
            return 2

        # Base case: 3 columns — There are exactly 5 distinct ways to fill a 2 x 3 board using dominoes and trominoes.
        if n == 3:
            return 5

        # Initialize a dp array to store the number of ways to tile a 2 x i board for all i from 0 to n.
        dp = [0] * (n + 1)

        # Fill in the base values
        dp[1] = 1  # One way to tile 2x1
        dp[2] = 2  # Two ways to tile 2x2
        dp[3] = 5  # Five ways to tile 2x3

        # Loop from 4 to n to compute dp[i] using recurrence relation
        for i in range(4, n + 1):
            # The recurrence relation:
            # dp[i] = 2 * dp[i - 1] + dp[i - 3]
            # 2 * dp[i - 1] comes from placing a vertical domino or a rotated tromino at the end.
            # dp[i - 3] comes from placing an L-shaped tromino in three new ways.
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD  # Take modulo at every step to prevent overflow

        return dp[n]  # Final result: number of ways to tile 2 x n board
