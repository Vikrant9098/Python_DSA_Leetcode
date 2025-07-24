class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Initialize a 2D list (dp table) with all values as 0
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # Fill the first column with 1s since only one way to move (all down)
        for i in range(m):
            dp[i][0] = 1

        # Fill the first row with 1s since only one way to move (all right)
        for j in range(n):
            dp[0][j] = 1

        # Fill the rest of the dp table using the relation:
        # dp[i][j] = dp[i-1][j] (from top) + dp[i][j-1] (from left)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # The bottom-right cell contains the total number of unique paths
        return dp[m - 1][n - 1]
