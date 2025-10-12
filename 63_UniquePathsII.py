class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        width = len(obstacleGrid[0])       # number of columns
        dp = [0] * width                    # 1D DP array to store paths for current row
        dp[0] = 1                           # start cell has 1 path

        for row in obstacleGrid:            # loop through each row
            for j in range(width):          # loop through each column
                if row[j] == 1:             # check if current cell is an obstacle
                    dp[j] = 0               # obstacle → no paths
                elif j > 0:                 # if not first column
                    dp[j] += dp[j - 1]     # add paths from left cell

        return dp[width - 1]                # total paths to bottom-right cell
