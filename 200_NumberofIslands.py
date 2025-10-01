class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # number of rows
        rows = len(grid)
        # number of columns
        cols = len(grid[0])
        # count of islands
        count = 0
        
        # iterate through each cell
        for i in range(rows):
            for j in range(cols):
                # if cell is land ('1'), start DFS
                if grid[i][j] == '1':
                    self.dfs(grid, i, j, rows, cols)
                    count += 1  # after DFS, increment island count
        return count
    
    def dfs(self, grid, i, j, rows, cols):
        # base case: out of bounds or water
        if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == '0':
            return
        
        # mark current cell as visited
        grid[i][j] = '0'
        
        # explore all 4 directions
        self.dfs(grid, i + 1, j, rows, cols)  # down
        self.dfs(grid, i - 1, j, rows, cols)  # up
        self.dfs(grid, i, j + 1, rows, cols)  # right
        self.dfs(grid, i, j - 1, rows, cols)  # left
