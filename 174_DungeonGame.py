class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)               # Number of rows
        n = len(dungeon[0])            # Number of columns

        dp = [[0] * n for _ in range(m)]   # DP table to store min health needed from (i, j)

        # Base case: princess's cell (bottom-right)
        dp[m - 1][n - 1] = max(1, 1 - dungeon[m - 1][n - 1])  # Need at least 1 HP to stay alive

        # Fill last row (can only move right)
        for j in range(n - 2, -1, -1):
            dp[m - 1][j] = max(1, dp[m - 1][j + 1] - dungeon[m - 1][j])  # Calculate from right to left

        # Fill last column (can only move down)
        for i in range(m - 2, -1, -1):
            dp[i][n - 1] = max(1, dp[i + 1][n - 1] - dungeon[i][n - 1])  # Calculate from bottom to top

        # Fill rest of the grid from bottom-right to top-left
        for i in range(m - 2, -1, -1):          # Loop rows upward
            for j in range(n - 2, -1, -1):      # Loop columns leftward
                min_health_next = min(dp[i + 1][j], dp[i][j + 1])   # Take min of right and down cell
                dp[i][j] = max(1, min_health_next - dungeon[i][j])  # Health needed at current cell

        return dp[0][0]   # Return min initial health needed at start (top-left)
