class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])  # number of rows and columns

        # Update first row: can only come from left
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]  # add value from left cell

        # Update first column: can only come from top
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]  # add value from top cell

        # Update rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                # Take minimum of top or left + current cell value
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        # Return the minimum path sum at bottom-right corner
        return grid[m - 1][n - 1]
