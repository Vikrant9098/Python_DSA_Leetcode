class Solution(object):
    def maxPathScore(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        # Get dimensions of the grid
        m, n = len(grid), len(grid[0])

        # Initialize a very small value (negative infinity)
        INF = float("-inf")

        # 3D DP array:
        # dp[i][j][c] = maximum score reaching cell (i, j) using c non-zero cells
        dp = [[[INF] * (k + 1) for _ in range(n)] for _ in range(m)]

        # Starting point (0,0) with 0 cost gives score 0
        dp[0][0][0] = 0

        # Traverse through each cell
        for i in range(m):
            for j in range(n):
                for c in range(k + 1):

                    # Skip if this state is not reachable
                    if dp[i][j][c] == INF:
                        continue

                    # Move DOWN (i+1, j)
                    if i + 1 < m:
                        val = grid[i + 1][j]

                        # Cost is 1 if cell value is non-zero, else 0
                        cost = 0 if val == 0 else 1

                        # Check if we can still stay within k cost
                        if c + cost <= k:
                            dp[i + 1][j][c + cost] = max(
                                dp[i + 1][j][c + cost],
                                dp[i][j][c] + val
                            )

                    # Move RIGHT (i, j+1)
                    if j + 1 < n:
                        val = grid[i][j + 1]

                        # Cost calculation same as above
                        cost = 0 if val == 0 else 1

                        if c + cost <= k:
                            dp[i][j + 1][c + cost] = max(
                                dp[i][j + 1][c + cost],
                                dp[i][j][c] + val
                            )

        # Get the maximum score at destination (m-1, n-1)
        ans = max(dp[m - 1][n - 1])

        # If no valid path found, return -1
        return -1 if ans < 0 else ans